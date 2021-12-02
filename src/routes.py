from flask import Flask, render_template, request, redirect
from db import db
from link_repository import LinkRepository

app = Flask(__name__)
LINK_REPOSITORY = LinkRepository(db.session)

@app.route("/")
def index():
    #argumenttina lukuvinkit = [...] jossa jokainen jäsen sisältää vähintään title ja link_url
    data = LINK_REPOSITORY.find_all()
    return render_template("home.html",lukuvinkit=data)

@app.route("/addlink")
def add_link():
    return render_template("createLink.html")

@app.route("/postlink", methods=["post"])
def post_link():
    title = request.form["title"]
    link_url = request.form["link_url"]
    data = {"title":title,
            "link_url":link_url}
    LINK_REPOSITORY.create(data)
    LINK_REPOSITORY.commit()
    return redirect("/")