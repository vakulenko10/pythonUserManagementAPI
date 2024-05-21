from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import uuid


app = Flask(__name__)
CORS(app) 
# Load users from the file at startup
def load_users():
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
        return users
    except FileNotFoundError:
        return []

# Save users to the file
def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file)

# Load users initially
users = load_users()

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    user_id = str(uuid.uuid4())  # Generate a unique ID
    new_user = {
        "id": user_id,
        "name": data.get("name"),
        "lastname": data.get("lastname"),
        "age": data.get("age")
    }
    users.append(new_user)
    save_users(users)
    return jsonify(new_user), 201


@app.route('/users/<string:user_id>', methods=['PUT'])
def edit_user(user_id):
    data = request.json
    for user in users:
        if user['id'] == user_id:
            user['name'] = data.get("name", user['name'])
            user['lastname'] = data.get("lastname", user['lastname'])
            user['age'] = data.get("age", user['age'])
            save_users(users)
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for i, user in enumerate(users):
        if user['id'] == user_id:
            deleted_user = users.pop(i)
            save_users(users)
            return jsonify(deleted_user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users/search', methods=['GET'])
def search_user():
    search_term = request.args.get('q', '').lower()
    results = [user for user in users if search_term in user['name'].lower() or search_term in user['lastname'].lower()]
    return jsonify(results)

@app.route('/users/sort', methods=['GET'])
def sort_users():
    sort_by = request.args.get('by', 'id')
    if sort_by == "name":
        users.sort(key=lambda user: user['name'].lower())
    elif sort_by == "lastname":
        users.sort(key=lambda user: user['lastname'].lower())
    elif sort_by == "age":
        users.sort(key=lambda user: int(user['age']))
    elif sort_by == "id":
        users.sort(key=lambda user: int(user['id']))
    else:
        return jsonify({"error": "Invalid sort parameter"}), 400

    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)