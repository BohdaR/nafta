from flask import request, Blueprint
from db.Brands import Brands

brand_api = Blueprint('brand_api', __name__, url_prefix='/api/v1')


@brand_api.get('/brands')
def index():
    return Brands().all()


@brand_api.get('/brands/<int:pk>')
def show(pk):
    return Brands().find(pk)


@brand_api.route('/brands', methods=['POST'])
def create():
    return Brands().create(request.form)


@brand_api.route('/brands/<int:pk>', methods=['POST', 'PUT', 'PATCH'])
def update(pk):
    return Brands().update(pk, **request.form)


@brand_api.route('/brands/<int:pk>', methods=['DELETE'])
def destroy(pk):
    return Brands().destroy(pk)
