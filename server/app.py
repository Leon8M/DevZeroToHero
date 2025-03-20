from flask import Flask
from flask_cors import CORS
from routes.tutorial_routes import tutorial_routes
from routes.user_routes import user_routes
from utils.db import init_db

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Register blueprints
app.register_blueprint(tutorial_routes, url_prefix="/api/tutorials")
app.register_blueprint(user_routes, url_prefix="/api/users")

# Initialize MongoDB
init_db(app)

@app.route("/")
def home():
    return "Welcome to DevZeroToHero Backend!"

if __name__ == "__main__":
    app.run(debug=True)