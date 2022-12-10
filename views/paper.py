from db.Papers import Papers
from flask import request, Blueprint

paper_api = Blueprint('paper_api', __name__, url_prefix='/api/v1')


@paper_api.get('/papers')
def index():
    return Papers().all()


@paper_api.get('/papers/<int:pk>')
def show(pk):
    return Papers().find(pk)


@paper_api.route('/papers', methods=['POST'])
def create():
    return Papers().create(request.json)


@paper_api.route('/papers/<int:pk>', methods=['POST', 'PUT', 'PATCH'])
def update(pk):
    return Papers().update(pk, **request.json)


@paper_api.route('/papers/<int:pk>', methods=['DELETE'])
def destroy(pk):
    return Papers().destroy(pk)
