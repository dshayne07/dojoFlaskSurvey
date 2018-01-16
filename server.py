from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key="oiwajefoaiwnegwboughuao"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    session["data"] = (request.form)
    return redirect("/display_results")

@app.route("/display_results")
def display():
    return render_template("results.html")

app.run(debug=True)