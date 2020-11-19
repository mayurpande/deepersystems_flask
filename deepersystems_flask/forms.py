from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import InputRequired
from deepersystems_flask.extentions import mongo


class HomePage(FlaskForm):

    video_name = StringField('Video Name')
    theme_name = StringField('Theme name')
    url = StringField('URL')


class LikeButtonForm(FlaskForm):
    submit = SubmitField('like')
    hidden = HiddenField('hidden')


class DisLikeButtonForm(FlaskForm):
    submit = SubmitField('dislike')
    hidden = HiddenField('hidden')







