from flask import request, Blueprint, render_template

from db.Papers import Papers

pages = Blueprint('pages', __name__)


@pages.get('/')
def index():
    context = {
        'papers': Papers().all(),
    }
    return render_template('index.html', **context)


@pages.get('/show')
def show():
    return render_template('index.html')
