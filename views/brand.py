from flask import request, Blueprint
from db.Brand import Brand

brand_api = Blueprint('brand_api', __name__)


@brand_api.get('/brands')
def index():
    return Brand().all()


@brand_api.get('/brands')
def show(pk):
    return Brand().find(pk)


@brand_api.route('/brands', methods=['POST', 'PUT', 'PATCH'])
def update(pk):
    return Brand().update(pk, **request.form)


@brand_api.route('/brands', methods=['POST'])
def create():
    return Brand().create(request.form)


@brand_api.route('/brands', methods=['DELETE'])
def destroy(pk):
    return Brand().destroy(pk)
