from flask import Flask
from config import Config
from database import db
from routes import register_routes
from models import User  # Import User model to create tables

# Create Flask app and configure it
app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

with app.app_context():
    db.create_all()



# Register routes from routes.py
register_routes(app)

# Create tables automatically if they don't exist

if __name__ == "__main__":
    app.run(debug=True)
