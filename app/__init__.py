from flask import Flask

from views.binding_type import binding_type_api
from views.brand import brand_api
from views.color import color_api
from views.country import country_api
from views.paper import paper_api
from views.paper_format import paper_format_api
from views.paper_type import paper_type_api
from views.papers_colors import papers_colors_api

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(paper_api)
app.register_blueprint(brand_api)
app.register_blueprint(binding_type_api)
app.register_blueprint(color_api)
app.register_blueprint(country_api)
app.register_blueprint(paper_format_api)
app.register_blueprint(paper_type_api)
app.register_blueprint(papers_colors_api)