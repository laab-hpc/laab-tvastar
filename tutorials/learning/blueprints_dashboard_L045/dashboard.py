from flask import Flask, Blueprint

app = Flask(__name__)

from .dashboard.app1 import routes as app1_routes
app.register_blueprint(app1_routes.bp, url_prefix='/')

from .dashboard.app2 import routes as app2_routes
app.register_blueprint(app2_routes.bp, url_prefix='/app2')