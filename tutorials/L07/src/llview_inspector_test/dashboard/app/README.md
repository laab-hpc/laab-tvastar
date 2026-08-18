# Tutorial

Let us first look at `routes.py`.

This file defines the routes for the dashboard app. Right now, it has two routes:

- `/`
- `/acknowledgements`

The `index()` function handles `/`, and the `acknowledgements()` function handles `/acknowledgements`.

In `index()`, we also read the environment variable `LAAB_DATA_DIR` and pass it into the template:

```python
return render_template('index.html', data_dir=data_dir)
```

That means the value becomes available inside `index.html` as `data_dir`.

## Why is the folder called `templates/`?

The folder is called `templates/` because this is the default place Flask looks for HTML templates.

In `routes.py`, the blueprint is created with:

```python
bp = Blueprint(
    name,
    __name__,
    template_folder="templates/",
)
```

So when we call:

```python
render_template('index.html')
```

Flask looks for `index.html` inside this `templates/` folder.

## Why do we need base.html?

We want two pages `index.html` and `achnowledgements.html`, and we want both of them to have the same navbar and footer. But we do not want to repeat that code twice.

That is why we create a `base.html`.

## What happens in `base.html`?

In `base.html`, we want a navbar and a footer, but we do not want to design them from scratch. So we reuse what Tvastar already provides.

At the top of `base.html`, you will see:

```html
{% extends 'tvst-bases/nav-top.html' %}
```

This means: use the contents of `tvst-bases/nav-top.html` as the starting template.

Where do we find `tvst-bases/`?

Remember that we registered the `tvastar` blueprint in `dashboard.py`. Inside `tvastar/tvastar.py`, the blueprint registers a `template` folder. Because of that, everything inside `tvastar/templates` folder becomes available to the app. That is why `tvst-bases/nav-top.html` can be found and extended here.

In `tvst-bases/nav-top.html`, you will find parts written with `{% block ... %}` and `{% endblock %}`. These are the sections that can be changed when another template extends it.

So when `app/templates/base.html` uses:

```html
{% extends 'tvst-bases/nav-top.html' %}
```

it can fill in or override those blocks at the places already defined in `tvst-bases/nav-top.html`.

In `base.html`, we modify:

- the page title
- the brand URL
- the brand name
- the navbar background color
- the left navbar items
- the right navbar items
- the footer
- the page content block

So now we have a base template that reuses the Tvastar design.

## Why do `index.html` and `acknowledgements.html` extend `base.html`?

Now we want this base for all our app pages.

That is why `index.html` starts with:

```html
{% extends 'base.html' %}
```

and `acknowledgements.html` does the same.

This means both pages reuse the same navbar, footer, and overall page layout, and only provide their own page-specific content.

So the flow in this folder is:

- `routes.py` defines the URLs
- `templates/base.html` defines the shared page layout
- `templates/index.html` fills the content block for the main page
- `templates/acknowledgements.html` fills the content block for the acknowledgements page

This is why the app stays clean: shared layout is written once, and each page only adds what is different.
