from flask import Blueprint, render_template, redirect, url_for
from deepersystems_flask.forms import HomePage, LikeButtonForm, DisLikeButtonForm
from deepersystems_flask.extentions import mongo

theme = Blueprint('theme', __name__)


@theme.route('/theme', methods=['GET', 'POST'])
def index():
    deep_coll = mongo.db.flaskapp
    themes = deep_coll.find()

    high_themes = []
    for theme in themes:
        dict_app = {}
        dict_app['theme_name'] = theme['theme_name']
        dict_app['score'] = theme['likes'] - (theme['dislikes']/2)
        high_themes.append(dict_app)

    high_themes = sorted(high_themes, key=lambda k: k['score'], reverse=True)

    return render_template('theme.html', high_themes=high_themes)

