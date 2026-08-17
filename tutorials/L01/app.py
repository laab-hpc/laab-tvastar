from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    title = "Performance Report"
    value = 42.5

    return render_template(
        "index.html",
        title=title,
        value=value
    )


if __name__ == "__main__":
    app.run(debug=True, port=8000)
