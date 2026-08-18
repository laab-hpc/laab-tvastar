from flask import Blueprint, render_template
import os

from pathlib import Path
name = Path(__file__).parent.name #report


bp = Blueprint(
    name,
    __name__,
    template_folder=f"templates/", # folder relative to this file!!! Note that same html files are used for different apps, there might be conflicts. Hence, we scope them under app specific folders.
)


@bp.route('/')
def index():
    data_dir = os.getenv("LAAB_DATA_DIR", "some_path/to/data_dir")  # Default value if the environment variable is not set
    
    ## Read and process the contents of the data dir 
    
    return render_template(f'index.html', data_dir=data_dir)

@bp.route('/acknowledgements')
def acknowledgements():
    return render_template(f'acknowledgements.html')