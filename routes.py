from app import app
from flask import render_template

@app.route("/")
def index():
    #argumenttina lukuvinkit = [...] jossa jokainen jäsen sisältää vähintään title ja link_url
    return render_template("home.html")

@app.route("/addlink")
def add_link():
    return render_template("createLink.html")

@app.route("/postlink", methods=["post"])
def post_link():
    #formissa title ja link_url
    pass