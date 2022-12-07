from flask import request, Blueprint
from db.Colors import Colors

color_api = Blueprint('color_api', __name__, url_prefix='/api/v1')


@color_api.get('/colors')
def index():
    return Colors().all()


@color_api.get('/colors/<int:pk>')
def show(pk):
    return Colors().find(pk)


@color_api.route('/colors', methods=['POST'])
def create():
    return Colors().create(request.form)


@color_api.route('/colors/<int:pk>', methods=['POST', 'PUT', 'PATCH'])
def update(pk):
    return Colors().update(pk, **request.form)


@color_api.route('/colors/<int:pk>', methods=['DELETE'])
def destroy(pk):
    return Colors().destroy(pk)
