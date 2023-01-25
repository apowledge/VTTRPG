from pathfinder import app
from flask import render_template, request, Blueprint, send_from_directory

@app.route("/")
@app.route("/home")
def home():
    return render_template("two-col-left-sidebar.html")
    #return render_template("base_bootstrap.html")
    #print("Display Home Page")
    #return render_template("temp.html")