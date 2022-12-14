from flask import request, Blueprint
from db.Countries import Countries

country_api = Blueprint('country_api', __name__, url_prefix='/api/v1')


@country_api.get('/countries')
def index():
    if request.args.get('name'):
        return Countries().filter('name', f"%{request.args.get('name')}%")
    return Countries().all()


@country_api.get('/countries/<int:pk>')
def show(pk):
    return Countries().find(pk)


@country_api.route('/countries', methods=['POST'])
def create():
    return Countries().create(request.json)


@country_api.route('/countries/<int:pk>', methods=['POST', 'PUT', 'PATCH'])
def update(pk):
    return Countries().update(pk, **request.json)


@country_api.route('/countries/<int:pk>', methods=['DELETE'])
def destroy(pk):
    return Countries().destroy(pk)
