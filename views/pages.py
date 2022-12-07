from flask import request, Blueprint, render_template

pages = Blueprint('pages', __name__)


@pages.get('/')
def index():
    # return render_template('index.html')
    return 'Hello'


@pages.get('/show')
def show():
    return render_template('index.html')
