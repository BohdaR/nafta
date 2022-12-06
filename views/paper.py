from db.Paper import Paper
from flask import request, Blueprint

paper_api = Blueprint('paper_api', __name__)


@paper_api.get('/papers')
def index():
    return Paper().all()


@paper_api.get('/papers')
def show(pk):
    return Paper().find(pk)


@paper_api.route('/papers', methods=['POST', 'PUT', 'PATCH'])
def update(pk):
    return Paper().update(pk, **request.form)


@paper_api.route('/papers', methods=['POST'])
def create():
    return Paper().create(request.form)


@paper_api.route('/papers', methods=['DELETE'])
def destroy(pk):
    return Paper().destroy(pk)
