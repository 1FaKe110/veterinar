from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PetForm(FlaskForm):
    name = StringField('Имя питомца', validators=[DataRequired()])
    species = StringField('Species', validators=[DataRequired()])
    submit = SubmitField('Add Pet')
