from flask import Flask, render_template, request, redirect
from db import configure_db
from link_repository import LinkRepository
from user_repository import UserRepository
import hashlib


app = Flask(__name__)
db = configure_db(app)
LINK_REPOSITORY = LinkRepository(db.session)
USER_REPOSITORY = UserRepository(db.session)

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

@app.route("/<int:link_id>")
def show_link(link_id):
    data = LINK_REPOSITORY.find({"id":link_id})

@app.route("/login")
def login():
    return render_template("/login.html")

@app.route("/register")
def register():
    return render_template("/register.html")

#event handlers
@app.route("/handleregister", methods=["POST"])
def handle_register():
    salted_password = request.form["password"]+"joiafhoufheoa3ijfla3dfnuneugyugeoj830803"
    hash = hashlib.sha256(salted_password.encode())
    data = {
        "username": request.form["username"],
        "password": hash.hexdigest()
    }
    USER_REPOSITORY.create(data)
    USER_REPOSITORY.commit()
    return redirect("/")

@app.route("/handlelogin", methods=["POST"])
def handle_login():
    pass




