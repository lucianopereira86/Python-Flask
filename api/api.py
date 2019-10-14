import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Users dictionary
users_dict = [{ 'id': 1, 'name': 'Luciano', 'age': 33 }, { 'id': 2, 'name': 'Paulo', 'age': 28 }]

# List all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users_dict)

# Get one user by id
@app.route('/user', methods=['GET'])
def get_user_by_id():
    # get parameter 'id' from request
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    
    for user in users_dict:
        if user['id'] == id:
            return jsonify(user)
    return {}

# Get one user by id from the path
@app.route("/user/<id>", methods=['GET'])
def get_user_by_id_in_path(id):
    for user in users_dict:
        if user['id'] == int(id):
            return jsonify(user)
    return {}

app.run()