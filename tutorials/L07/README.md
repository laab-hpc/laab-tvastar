# L07 - Integrating Tvastar

This lesson is about more than getting a Flask dashboard to run. It is also about learning how to place a software component inside a repository in a way that still makes sense when the repository grows.

First, look into the `pyproject.toml`.

The variable `name` is the name of the Python package we want to build. In this case, it is `llview_inspector_test`.


```toml
[project]
name = "llview_inspector_test"
```

This line tells us the name of the Python package for this project.

The following lines say: look for the folder `llview_inspector_test` inside `src/`.

```toml
[tool.setuptools.packages.find]
where = ["src"]
```

So we have a directory called `src/`, and we place `llview_inspector_test` inside it. You can rename `src/` if you want, but we will try to stick to the standard. This is important because it makes the project easier for someone else to understand, even without your attention.

## Why not put `llview_inspector_test` directly at the top?

In principle, one could delete:

```toml
where = ["src"] 
```

and have this folder structure:

```text
L07/
├── pyproject.toml
└── llview_inspector_test/
```

But we do not want that.

Why?

Because `llview_inspector_test` is only one component of a potentially larger repository.

Today, `src/` contains only:

```text
src/
└── llview_inspector_test/
```

But later, the same `src/` directory may look like this:

```text
src/
├── llview_inspector_test/
├── benchmark_codes/
└── another_component/
```

And that matters.

`benchmark_codes/` might contain C code, a standalone benchmark, or some other implementation that has nothing to do with the Python package itself. It still belongs to the repository, and it still belongs under `src/`, but it does not need to become part of `llview_inspector_test`.

That is the reason for this layout: the repository is bigger than one package name.


Now go to the README inside `src/` to learn more about what is there.

## Install

Prepare the virtual environment. You only need to do this once.

```bash
ml GCC SciPy-bundle
python -m venv venv --system-site-packages
```

## Run dashboard

Activate the virtual environment first.

```bash
ml GCC SciPy-bundle
source venv/bin/activate
laab-dashboard
```

You need to run `ml GCC SciPy-bundle` every time you open a new terminal.

This opens the web app on port `8000`.
