import os
from flask import Flask, render_template, request, redirect, session

from db import configure_db
from link_repository import LinkRepository
from user_repository import UserRepository


app = Flask(__name__)
db = configure_db(app)
LINK_REPOSITORY = LinkRepository(db.session)
USER_REPOSITORY = UserRepository(db.session)
SECRET_KEY = os.environ.get("SECRET_KEY")
app.secret_key = SECRET_KEY


@app.route("/")
def index():
    # argumenttina lukuvinkit = [...] jossa jokainen jäsen sisältää vähintään title ja link_url
    data = LINK_REPOSITORY.find_all()
    return render_template("home.html", lukuvinkit=data)


@app.route("/addlink")
def add_link():
    if "id" not in session:
        return render_template("createLink.html",
            error_message="Sinun tulee kirjautua sisään ennen kuin voit lisätä lukuvinkkejä")
    return render_template("createLink.html")


@app.route("/postlink", methods=["post"])
def post_link():
    title = request.form["title"]
    link_url = request.form["link_url"]
    data = {"title":title,
            "link_url":link_url,
            "created_by": session["id"]}
    LINK_REPOSITORY.create(data)
    LINK_REPOSITORY.commit()
    return redirect("/")

@app.route("/links/<int:link_id>")
def show_link(link_id):
    data = LINK_REPOSITORY.find({"id":link_id})
    return render_template("lukuvinkki.html", lukuvinkki=data)
@app.route("/lukuvinkki_haku")

def haku():
    data = LINK_REPOSITORY.find_all()
    data = filter(lambda x: request.args.get("search") in f"${x.title}{x.link_url}", data)
    return render_template("home.html", lukuvinkit=data)

@app.route("/login")
def login():
    return render_template("/login.html")


@app.route("/register")
def register():
    return render_template("/register.html")

# event handlers


@app.route("/handleregister", methods=["POST"])
def handle_register():
    input_password = request.form["password"]
    input_username = request.form["username"]
    state = USER_REPOSITORY.register({"username":input_username,
                            "password":input_password})

    if not state:
        return render_template("register.html", error_message="Käyttäjänimi on jo käytössä")
    return redirect("/login")


@app.route("/handlelogin", methods=["POST"])
def handle_login():
    input_password = request.form["password"]
    input_username = request.form["username"]
    try:
        user = USER_REPOSITORY.login({"username":input_username,
                                "password":input_password})

    except Exception:
        return render_template("login.html",
            error_message="Virheellinen käyttäjänimi tai salasana.")
    session["id"] = user["id"]
    session["username"]=user["username"]
    return redirect("/")

@app.route("/handlelogout")
def handle_logout():
    del session["id"]
    del session["username"]
    return redirect("/")
