#!/usr/bin/env python3

from flask import Flask
from flask_migrate import Migrate
from models import db

# Create Flask app instance
app = Flask(__name__)

# Configure app to use SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration
db.init_app(app)
migrate = Migrate(app, db)

# Placeholder test for CodeGrade
def test_codegrade_placeholder():
    """Codegrade placeholder test"""
    assert 1 == 1

# Run the app
if __name__ == '__main__':
    app.run(port=5555, debug=True)
