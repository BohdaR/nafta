from flask import request, Blueprint, render_template

from db.BindingTypes import BindingTypes
from db.Brands import Brands
from db.Countries import Countries
from db.PaperFormats import PaperFormats
from db.PaperTypes import PaperTypes
from db.Papers import Papers

pages = Blueprint('pages', __name__)


@pages.get('/')
def papers():
    wanted_columns = ['name', 'description', 'pieces', 'density', 'status']
    join_params = {
        ('binding_types', 'name'): "biting_type",
        ('brands', 'name'): "brand_name",
        ('countries', 'name'): "country_name",
        ('paper_formats', 'name'): "paper_format",
        ('paper_types', 'name'): "paper_type"
    }
    context = {
        'papers': Papers().join(wanted_columns, join_params),
    }
    return render_template('papers.html', **context)


@pages.get('/brands')
def brands():
    wanted_columns = ['name', ]
    join_params = {
        ('countries', 'name'): "country_name",
    }
    context = {
        'brands': Brands().join(wanted_columns, join_params),
    }
    return render_template('brands.html', **context)


@pages.get('/countries')
def countries():
    context = {
        'countries': Countries().all(),
    }
    return render_template('countries.html', **context)


@pages.get('/paper_formats')
def paper_formats():
    context = {
        'paper_formats': PaperFormats().all(),
    }
    return render_template('paper_formats.html', **context)


@pages.get('/paper_types')
def paper_types():
    context = {
        'paper_types': PaperTypes().all(),
    }
    return render_template('paper_types.html', **context)


@pages.get('/binding_types')
def binding_types():
    context = {
        'binding_types': BindingTypes().all(),
    }
    return render_template('binding_types.html', **context)
