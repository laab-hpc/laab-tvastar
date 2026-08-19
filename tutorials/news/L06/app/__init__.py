## Application Factory
## create_app() replaces former app = Flask(__name__)

from flask import Flask
from app.dashboard.routes import dashboard_bp

def create_app(): 
    app = Flask(__name__)
    app.register_blueprint(dashboard_bp)

    return app
