from flask import Blueprint, render_template, redirect, url_for
from deepersystems_flask.forms import HomePage, LikeButtonForm, DisLikeButtonForm
from deepersystems_flask.extentions import mongo
from bson.objectid import ObjectId

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    deep_coll = mongo.db.flaskapp
    vids = deep_coll.find()
    form = HomePage()
    likes = LikeButtonForm()
    dislikes = DisLikeButtonForm()

    if form.validate_on_submit():

        video_name = form.video_name.data
        theme_name = form.theme_name.data
        deep_coll.insert({'video_name': video_name, 'theme_name': theme_name, 'likes': 0, 'dislikes': 0})

    return render_template('index.html', form=form, vids=vids, likes=likes, dislikes=dislikes)


@main.route('/likes', methods=['POST'])
def likes():

    likes = LikeButtonForm()
    coll = mongo.db.flaskapp
    post = coll.find_one({'_id': ObjectId(likes.hidden.data)})
    post['likes'] += 1
    coll.update_one({'_id': ObjectId(likes.hidden.data)}, {"$set": post}, upsert=False)

    return redirect(url_for('main.index'))


@main.route('/dislikes', methods=['POST'])
def dislikes():

    dislikes = DisLikeButtonForm()
    coll = mongo.db.flaskapp
    post = coll.find_one({"_id": ObjectId(dislikes.hidden.data)})
    post['dislikes'] += 1
    coll.update_one({'_id': ObjectId(dislikes.hidden.data)}, {"$set": post}, upsert=False)

    return redirect(url_for('main.index'))
