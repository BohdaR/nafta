from flask import request, Blueprint
from db.PaperTypes import PaperTypes

paper_type_api = Blueprint('paper_type_api', __name__)


@paper_type_api.get('/paper_types')
def index():
    return PaperTypes().all()


@paper_type_api.get('/paper_types/<int:pk>')
def show(pk):
    return PaperTypes().find(pk)


@paper_type_api.route('/paper_types', methods=['POST'])
def create():
    return PaperTypes().create(request.form)


@paper_type_api.route('/paper_types/<int:pk>', methods=['POST', 'PUT', 'PATCH'])
def update(pk):
    return PaperTypes().update(pk, **request.form)


@paper_type_api.route('/paper_types/<int:pk>', methods=['DELETE'])
def destroy(pk):
    return PaperTypes().destroy(pk)