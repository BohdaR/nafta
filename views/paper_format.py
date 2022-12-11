from flask import request, Blueprint
from db.PaperFormats import PaperFormats

paper_format_api = Blueprint('paper_format_api', __name__, url_prefix='/api/v1')


@paper_format_api.get('/paper_formats')
def index():
    if request.args.get('name'):
        return PaperFormats().filter('name', f"%{request.args.get('name')}%")
    return PaperFormats().all()


@paper_format_api.get('/paper_formats/<int:pk>')
def show(pk):
    return PaperFormats().find(pk)


@paper_format_api.route('/paper_formats', methods=['POST'])
def create():
    return PaperFormats().create(request.json)


@paper_format_api.route('/paper_formats/<int:pk>', methods=['POST', 'PUT', 'PATCH'])
def update(pk):
    return PaperFormats().update(pk, **request.json)


@paper_format_api.route('/paper_formats/<int:pk>', methods=['DELETE'])
def destroy(pk):
    return PaperFormats().destroy(pk)
