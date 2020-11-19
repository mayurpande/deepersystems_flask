from flask import Blueprint, render_template, flash, redirect, request
from deepersystems_flask.forms import HomePage
from deepersystems_flask.extentions import mongo

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    deep_coll = mongo.db.deeper.flaskapp
    vids = deep_coll.find()
    form = HomePage()

    if form.validate_on_submit():

        video_name = form.video_name.data
        theme_name = form.theme_name.data
        deep_coll.insert({'video_name': video_name, 'theme_name': theme_name, 'complete': False})

    return render_template('index.html', form=form, vids=vids)


