from flask import Blueprint, request, jsonify
from models import User

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/", methods=["POST"])
def create_user():
    data = request.json
    user = User.create_user(
        username=data["username"],
        email=data["email"],
        password=data["password"],
    )
    return jsonify({"message": "User created!", "id": str(user.inserted_id)})