from flask import request, Blueprint, render_template, redirect, url_for

from db.BindingTypes import BindingTypes
from db.Brands import Brands
from db.Countries import Countries
from db.PaperFormats import PaperFormats
from db.PaperTypes import PaperTypes
from db.Papers import Papers

pages = Blueprint('pages', __name__)


@pages.get('/')
def papers():
    context = {
        'papers': Papers().all(),
        'brands': Brands().all(),
        'paper_types': PaperTypes().all(),
        'paper_formats': PaperFormats().all(),
        'binding_types': BindingTypes().all(),
        'countries': Countries().all(),
    }
    return render_template('papers.html', **context)


@pages.get('/brands')
def brands():
    context = {
        'brands': Brands().all(),
        'countries': Countries().all(),
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
