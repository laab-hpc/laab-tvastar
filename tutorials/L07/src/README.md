# Tutorial

Now we are inside `src/`. There are two components here.

`benchmark_code/` is not touched by the `pyproject.toml` installation. This is almost empty for now. The idea is that, in the future, we place some benchmark code here. That code may generate files with measurement values, and `llview_inspector_test` will take those files as input, process them, and present them in a dashboard.

`llview_inspector_test/` is the part that gets built. After a successful installation with `pip install -e .` from the previous directory, a module named `llview_inspector_test` becomes available for import.

For example:

```python
import llview_inspector_test
```

Inside `llview_inspector_test/`, we have a module called `dashboard/`.

Again, `dashboard/` is just one part of `llview_inspector_test`, so we keep it in a separate folder. There is also another dummy component now, `data_processor/`, which has nothing to do with the dashboard.

This is also a good place to understand what a module or package means in Python.

A folder becomes a regular Python package when it contains an `__init__.py` file. That is why you see `__init__.py` in directories such as `dashboard/`, `app/`, and `tvastar/`.

Why do we keep `__init__.py`?

- It tells Python that this folder should be treated as a package.
- It allows us to organize code into subpackages and import from them in a clean way.

If we remove `__init__.py`, then some imports that we expect to work may stop working, especially when the code is called from a different directory or through an installed entry point.

For example, in this project we want imports like this to work reliably:

```python
from llview_inspector_test.dashboard.app import routes
```

If folders such as `dashboard/`, `app/`, or `tvastar/` do not have `__init__.py`, then Python may no longer recognize them properly as part of the package structure in the way we expect for this tutorial. That can lead to imports failing when the program is started from another location rather than from the same folder by hand.

So the story inside `src/` is simple:

- `benchmark_code/` can hold code that produces measurement data
- `llview_inspector_test/` can read and process that data
- `dashboard/` can present the results
- `data_processor/` is also there, but it is empty for now, so you can ignore it for this tutorial

Now go to the README inside `llview_inspector_test/dashboard` to continue the story from there.
