# Tutorial

This is a Flask app with two components.

1. `tvastar/`: this is treated as a library. It provides UI components and reusable designs. You do not have to touch it.
2. `app/`: this is the dashboard app we care about. It uses `tvastar/`.

Now let us look at what is inside `dashboard.py`.

In `dashboard.py`, we create the main Flask application:

```python
app = Flask(__name__)
```

After that, we import two blueprints.

The first import is:

```python
from .tvastar import tvastar
```

The second import is:

```python
from .app import routes
```

These imports work because `dashboard/`, `tvastar/`, and `app/` are treated as Python packages. That is why the `__init__.py` files matter here. For example, imports like `from .tvastar import tvastar` are part of this package structure and are expected to work reliably when the application is run through the installed package.

Next, we register the blueprints:

```python
app.register_blueprint(tvastar.bp, url_prefix=f'/{tvastar.name}')
app.register_blueprint(routes.bp, url_prefix=f'/')
```

Registering a blueprint means: take the routes, templates, static files, and related behavior from that component and attach them to the main Flask app.

The `url_prefix` tells Flask what starting path to put in front of the URLs from that blueprint.

For example:

- if a blueprint has a route `/hello` and the `url_prefix` is `/demo`, then the final URL becomes `/demo/hello`
- if a blueprint has a route `/` and the `url_prefix` is `/demo`, then the final URL becomes `/demo/`

In this project, `app/` is registered with:

```python
url_prefix='/'
```

So the routes inside `app/routes.py` become the main dashboard URLs.

Right now, the `app/` blueprint has these routes:

- `/`
- `/acknowledgements`

So when you run the app, these are the main pages you can visit.

The `tvastar/` blueprint is registered with:

```python
url_prefix=f'/{tvastar.name}'
```

Since `tvastar.name` comes from the filename `tvastar.py`, the prefix becomes `/tvastar`.

In this tutorial setup, `tvastar/` is not being used as a place for user-facing page routes. Instead, it mainly provides reusable templates, styles, script imports, and static assets that the main `app/` pages can build on top of.

So the story in `dashboard/` is:

- `dashboard.py` creates the Flask app
- `tvastar/` provides reusable UI building blocks
- `app/` provides the actual dashboard pages

Now go inside `app/` to find out more about the templates.
