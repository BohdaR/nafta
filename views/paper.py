from db.Papers import Papers
from flask import request, Blueprint, abort

paper_api = Blueprint('paper_api', __name__, url_prefix='/api/v1')


def check_params(params):
    if params.get('pieces'):
        if params.get('pieces', 0) == '':
            abort(400, description={'massage': "Field pieces can't be empty"})
        elif int(params.get('pieces')) <= 0:
            abort(400, description={'massage': 'Field pieces must be greater than 0'})

    if params.get('density'):
        if params.get('density', 0) == '':
            abort(400, description={'massage': "Field density can't be empty"})
        elif float(params.get('density', 0)) <= 0:
            abort(400, description={'massage': 'Field density must be greater than 0'})


@paper_api.get('/papers')
def index():
    return Papers().all()


@paper_api.get('/papers/<int:pk>')
def show(pk):
    return Papers().find(pk)


@paper_api.route('/papers', methods=['POST'])
def create():
    check_params(request.json)
    return Papers().create(request.json)


@paper_api.route('/papers/<int:pk>', methods=['POST', 'PUT', 'PATCH'])
def update(pk):
    check_params(request.json)
    return Papers().update(pk, **request.json)


@paper_api.route('/papers/<int:pk>', methods=['DELETE'])
def destroy(pk):
    return Papers().destroy(pk)
