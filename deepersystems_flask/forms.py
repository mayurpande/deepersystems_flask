from flask_wtf import FlaskForm
from wtforms import StringField, Form, FormField
from wtforms.validators import InputRequired, ValidationError
import re


class HomePage(FlaskForm):

    video_name = StringField('Video Name', validators=[InputRequired()])
    theme_name = StringField('Theme name', validators=[InputRequired()])
