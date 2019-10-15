import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Users dictionary
users_dict = []

# List all users
@app.route('/users', methods=['GET'])
def get_users():
    users = []
    for user in users_dict:
        contProp = 0
        for arg in request.args:
            val = user[arg]
            param = request.args[arg]
            if isinstance(val, int):
                param = int(param)
            if isinstance(val, str):
                val = val.upper()
                param = param.upper()
            if val == param:
                contProp += 1
        if contProp == len(request.args):
            users.append(user)
            
    return jsonify(users)

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


# Add new user
@app.route('/user', methods=['POST'])
def post_users():
    user = request.get_json()
    user['id'] = len(users_dict) + 1
    users_dict.append(user)
    return jsonify(user)

app.run()