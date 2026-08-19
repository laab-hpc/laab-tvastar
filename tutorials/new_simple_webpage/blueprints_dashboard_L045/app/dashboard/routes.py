from flask import Blueprint, render_template

dashboard_bp = Blueprint(
    "dashboard", 
    __name__, 
    url_prefix = "/dashboard"
    )

@dashboard_bp.route("/")
def index():
    head = "Dashboard"
    title = "Performance Report"
    version = 1.0

    kpis = [
        {
            "name": "Users",
            "value": 128,
        },
        {
            "name": "Revenue",
            "value": "12,457 €",
        },
        {
            "name": "Orders",
            "value": 324,
        },
    ]
    libraries = [
        "OpenBLAS",
        "MKL",
        "AOCL"
        ]
    results = [
        {"library": "OpenBLAS", "gflops": 120},
        {"library": "MKL",      "gflops": 145},
        {"library": "AOCL",     "gflops": 138}
        ]
    
    return render_template(
        "dashboard/index.html",
        head=head,
        title=title,
        version=version,
        kpis=kpis,
        libraries=libraries,
        results=results
        )