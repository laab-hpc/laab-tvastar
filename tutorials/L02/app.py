from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    title = "Performance Report"
    version = 1.0
    libraries = [
        "OpenBLAS",
        "MKL",
        "AOCL"
    ]
    results = [
        {"library": "OpenBLAS", "gflops": 120},
        {"library": "MKL",      "gflops": 145},
        {"library": "AOCL",     "gflops": 138},
    ]
 
    

    return render_template(
        "index.html",
        title=title,
        version=version,
        libraries=libraries,
        results=results
    )
    

if __name__ == "__main__":
    app.run(debug=True, port=8000)
