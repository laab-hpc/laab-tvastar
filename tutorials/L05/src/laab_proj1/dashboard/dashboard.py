from flask import Flask, Blueprint

app = Flask(__name__)

from .app1 import routes as app1_routes
app.register_blueprint(app1_routes.bp, url_prefix='/')

from .app2 import routes as app2_routes
app.register_blueprint(app2_routes.bp, url_prefix='/app2')


def main():
    app.run(debug=True, port=8000)

if __name__ == "__main__":
    main()