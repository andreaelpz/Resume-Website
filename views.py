from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/home")
def desktop():
    return render_template("desktop.html")

@views.route("/about")
def about():
    return render_template("about.html")

@views.route("/experience")
def experience():
    return render_template("experience.html")

@views.route("/resume")
def resume():
    return render_template("resume.html")

@views.route("/email")
def email():
    return render_template("email.html")

