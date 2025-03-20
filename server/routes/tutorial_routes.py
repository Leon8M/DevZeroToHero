from flask import Blueprint, request, jsonify
from models import Tutorial

tutorial_routes = Blueprint("tutorial_routes", __name__)

@tutorial_routes.route("/", methods=["GET"])
def get_tutorials():
    tutorials = Tutorial.get_tutorials()
    return jsonify(tutorials)

@tutorial_routes.route("/", methods=["POST"])
def create_tutorial():
    data = request.json
    tutorial = Tutorial.create_tutorial(
        title=data["title"],
        description=data["description"],
        content=data["content"],
        category=data["category"],
        author_id=data["author_id"],
    )
    return jsonify({"message": "Tutorial created!", "id": str(tutorial.inserted_id)})