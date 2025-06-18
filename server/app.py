#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Earthquake

# ✅ Create the Flask app first
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# ✅ Setup DB + Migrate
migrate = Migrate(app, db)
db.init_app(app)

# ✅ Define your routes *after* the app is created
@app.route('/')
def index():
    return make_response({"message": "Flask SQLAlchemy Lab 1"}, 200)


@app.route('/earthquakes/<int:id>')
def get_earthquake_by_id(id):
    quake = Earthquake.query.filter_by(id=id).first()
    if quake:
        return make_response(quake.to_dict(), 200)
    return make_response({"message": f"Earthquake {id} not found."}, 404)


@app.route('/earthquakes/magnitude/<float:magnitude>')
def get_earthquakes_by_magnitude(magnitude):
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    return make_response({
        "count": len(quakes),
        "quakes": [q.to_dict() for q in quakes]
    }, 200)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
