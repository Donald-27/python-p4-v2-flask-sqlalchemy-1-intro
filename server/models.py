from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Create metadata and pass it to SQLAlchemy
metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

# Define the Pet model
class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
