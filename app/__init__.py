from flask import Flask

from views.brand import brand_api
from views.paper import paper_api

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(paper_api)
app.register_blueprint(brand_api)
