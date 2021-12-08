"""Models for AdoptWebApp"""


# Setup

from enum import unique
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.orm import backref, relationship

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.
    To be call in app file
    """

    db.app = app
    db.init_app(app)

#############################################################################

# Models


class Pet(db.Model):
    """pet model for the app"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(
        db.Text, default="https://tacm.com/wp-content/uploads/2018/01/no-image-available.jpeg")
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, default=True)
