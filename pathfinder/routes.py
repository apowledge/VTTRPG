from flask import render_template, request, Blueprint, send_from_directory

@app.route("/")
def home():
    #return render_template("two-col-left-sidebar.html")
    #return render_template("base_bootstrap.html")
    return render_template("temp.html")