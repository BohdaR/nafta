from flask import request, Blueprint
from db.PaperFormats import PaperFormats

paper_format_api = Blueprint('paper_format_api', __name__)


@paper_format_api.get('/paper_formats')
def index():
    return PaperFormats().all()


@paper_format_api.get('/paper_formats/<int:pk>')
def show(pk):
    return PaperFormats().find(pk)


@paper_format_api.route('/paper_formats', methods=['POST'])
def create():
    return PaperFormats().create(request.form)


@paper_format_api.route('/paper_formats/<int:pk>', methods=['POST', 'PUT', 'PATCH'])
def update(pk):
    return PaperFormats().update(pk, **request.form)


@paper_format_api.route('/paper_formats/<int:pk>', methods=['DELETE'])
def destroy(pk):
    return PaperFormats().destroy(pk)
