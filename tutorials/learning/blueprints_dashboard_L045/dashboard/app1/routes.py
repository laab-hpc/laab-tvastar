from flask import Blueprint, render_template

from pathlib import Path
name = Path(__file__).parent.name # app1


bp = Blueprint(
    name,
    __name__,
    template_folder=f"templates/", # folder relative to this file!!! Note that same html files are used for different apps, there might be conflicts. Hence, we scope them under app specific folders.
)


@bp.route('/')
def index():
    return render_template(f'{name}/index.html')