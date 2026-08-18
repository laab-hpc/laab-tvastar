from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    heading = "Performance Report"
    version = 1.0
    value = 42.8

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
        title=heading,
        version=version,
        libraries=libraries,
        results=results,
        value=value
    )

@app.route("/help")
def help():
    title = "Help"
    message = "This is the help page of the application."
    
    return render_template(
        "help.html",
        title=title,
        message=message
    )

#def hello_world():
    #return "<p>Hello World</p>"

if __name__ == "__main__":
    app.run(debug=True, port=8002)


