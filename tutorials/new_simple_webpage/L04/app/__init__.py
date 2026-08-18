## Application Factory
## create_app() replaces former app = Flask(__name__)

from flask import Flask

def create_app(): 
    app = Flask(__name__)

    return app
