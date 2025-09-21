from flask import Flask, jsonify, request

app = Flask(__name__)

# simulate database in memory
user = {}

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):  
    u = user.get(user_id)
    if u:
        return jsonify({"id": user_id, "name": u}), 200
    return jsonify({"error": "user not found"}), 400


@app.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = data.get("id")
    name = data.get("name")

    if not user_id or not name:
        return jsonify({"error": "invalid data"}), 400
    if user_id in user:
        return jsonify({"error": "user already exist"}), 400

    user[user_id] = name
    return jsonify({"id": user_id, "name": name}), 201