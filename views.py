from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/home")
def desktop():
    return render_template("desktop.html")

@views.route("/about")
def desktop():
    return render_template("about.html")

@views.route("/experience")
def desktop():
    return render_template("experience.html")

@views.route("/resume")
def desktop():
    return render_template("resume.html")