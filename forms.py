from typing import Optional
from flask_wtf import FlaskForm
from werkzeug.datastructures import Range
from wtforms import StringField, IntegerField, SelectField
from wtforms.fields.simple import BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Pet species", choices=[
                          ('cat', 'cat'), ('dog', 'dog'), ('porcupine', 'porcupine'), ('wolf', 'wolf')])
    photo = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Pet age", validators=[
        Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes", validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for editingpets"""

    photo = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Notes", validators=[Optional()])
    available = SelectField("Availability", choices=[
                            ('yes', 'yes'), ('no', 'no')])
