from flask import request, Blueprint
from db.BindingTypes import BindingTypes

binding_type_api = Blueprint('binding_type_api', __name__, url_prefix='/api/v1')


@binding_type_api.get('/binding_types')
def index():
    return BindingTypes().all()


@binding_type_api.get('/binding_types/<int:pk>')
def show(pk):
    return BindingTypes().find(pk)


@binding_type_api.route('/binding_types', methods=['POST'])
def create():
    return BindingTypes().create(request.json)


@binding_type_api.route('/binding_types/<int:pk>', methods=['POST', 'PUT', 'PATCH'])
def update(pk):
    return BindingTypes().update(pk, **request.json)


@binding_type_api.route('/binding_types/<int:pk>', methods=['DELETE'])
def destroy(pk):
    return BindingTypes().destroy(pk)
