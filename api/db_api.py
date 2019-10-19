import flask
from flask import request, jsonify
import sqlite3
from sqlite3 import Error
from flasgger.utils import swag_from
from flasgger import APISpec, Schema, Swagger, fields
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin


# Create an APISpec
spec = APISpec(
    title='Flasgger User API',
    version='1.0.0',
    openapi_version='1.0',
    plugins=[
        FlaskPlugin(),
        MarshmallowPlugin(),
    ],
)

class UserCategorySchema(Schema):
    id = fields.Int()
    age = fields.Int()
    name = fields.Str(required=True)

class UserSchema(Schema):
    category = fields.Nested(UserCategorySchema, many=True)
    name = fields.Str()


app = flask.Flask(__name__)
app.config["DEBUG"] = True

database = r"api/test.db"

# Simple Functions


def create_connection():
    c = None
    try:
        c = sqlite3.connect(database)
        print(sqlite3.version)
        return c
    except Error as e:
        print(e)


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
    finally:
        if c:
            c.close()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def execute(sql, isSelect=True):
    conn = sqlite3.connect(database)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    if isSelect:
        return cur.execute(sql).fetchall()
    else:
        result = cur.execute(sql)
        conn.commit()
        return result


def start_db():

    # create a database connection
    conn = create_connection()

    # create tables
    if conn is not None:
        user_table_sql = """ CREATE TABLE IF NOT EXISTS user (
                            id integer PRIMARY KEY AUTOINCREMENT,
                            age integer NOT NULL,
                            name text NOT NULL
                        ); """
        create_table(conn, user_table_sql)
    else:
        print("Error! cannot create the database connection.")

# HTTP functions

# Add new user
@app.route('/user', methods=['POST'])
def post_users():
    user = request.get_json()
    _age = user['age']
    _name = user['name']

    sql = f"INSERT INTO user (age, name) VALUES ({_age}, '{_name}');"

    result = execute(sql, False)
    user['id'] = result.lastrowid
    return jsonify(user)

# Update user
@app.route('/user', methods=['PUT'])
def put_users():
    user = request.get_json()
    _id = user['id']
    _age = user['age']
    _name = user['name']

    sql = f"UPDATE user SET age = {_age}, name = '{_name}' WHERE id = {_id};"
    execute(sql, False)
    return {}

# List all users
@app.route('/users', methods=['GET'])
@swag_from('yml/get.yml')
def get_users():

    _id = request.args['id'] if 'id' in request.args else 0
    _age = request.args['age'] if 'age' in request.args else 0
    _name = request.args['name'] if 'name' in request.args else ''

    sql = f"""SELECT * FROM user WHERE 
            ({_id} = 0 OR id = {_id}) 
            AND ({_age} = 0 OR age = {_age}) 
            AND ('{_name}' = '' OR UPPER(name) = UPPER('{_name}'));"""

    users = execute(sql)
    return jsonify(users)
    # return UserSchema().dump(users).data

# Delete user by id
@app.route('/user/<_id>', methods=['DELETE'])
def delete_users(_id):
    sql = f"DELETE FROM user WHERE id = {int(_id)};"
    execute(sql, False)
    return {}



template = spec.to_flasgger(
    app,
    definitions=[UserCategorySchema, UserSchema],
    paths=[get_users]
)

# start Flasgger using a template from apispec
swag = Swagger(app, template=template)

start_db()

app.run()
