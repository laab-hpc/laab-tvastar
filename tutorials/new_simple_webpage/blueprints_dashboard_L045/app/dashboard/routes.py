from flask import Blueprint, render_template
from app.dashboard.data import head, title, version, kpis, libraries, get_results

dashboard_bp = Blueprint(
    "dashboard", 
    __name__, 
    url_prefix = "/dashboard"
    )

@dashboard_bp.route("/")
def index():
    results = get_results()
    
    return render_template(
        "dashboard/index.html",
        head=head,
        title=title,
        version=version,
        kpis=kpis,
        libraries=libraries,
        results=results
        )