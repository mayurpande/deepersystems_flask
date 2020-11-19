from flask import Blueprint, render_template, flash, redirect, request

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')
