from db.Papers import Papers
from flask import request, Blueprint

papers_colors_api = Blueprint('papers_colors_api', __name__, url_prefix='/api/v1')


@papers_colors_api.get('/papers/<int:pk>/colors')
def index(pk):
    return Papers().all_target_records(pk, 'colors', 'papers_colors')


@papers_colors_api.get('/papers/<int:pk>/colors/<int:target_id>')
def show(pk, target_id):
    return Papers().find_target_record(pk, 'colors', 'papers_colors', target_id)


@papers_colors_api.post('/papers/<int:pk>/colors')
def create(pk):
    return Papers().add_target_record(pk, 'colors', 'papers_colors', request.form['color_id'])


@papers_colors_api.delete('/papers/<int:pk>/colors/<int:target_id>')
def destroy(pk, target_id):
    return Papers().remove_target_record(pk, 'colors', 'papers_colors', target_id)
