import os
from flask import Flask, Blueprint

def main():
    
    app = Flask(__name__)

    # for access to base templates, macros, styles and script imports
    from .tvastar import tvastar
    app.register_blueprint(tvastar.bp, url_prefix=f'/{tvastar.name}')
    
    from .app import routes
    app.register_blueprint(routes.bp, url_prefix=f'/')
    app.run(debug=True, port=8002)
    
if __name__ == '__main__':
    main()