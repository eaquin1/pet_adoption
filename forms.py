from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, Length, NumberRange

class EditPetForm(FlaskForm):
    """Form for editing pets"""

    photo_url = StringField("Image URL", validators=[Optional(), URL()])
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=5)])
    available = BooleanField("Available?")

class AddPetForm(FlaskForm):
    """Form for adding a pet"""

    name = StringField("Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo_url = StringField("Image URL", validators=[URL(), Optional()])
    age = FloatField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Comments", validators=[Optional()])
    available = BooleanField("Available?", validators=[Optional()])

