# export FLASK_APP=app.py && python3 -m flask run

from directions import directions as babo_direct
from locations_selectable import selectable_locations_dict as locations_dict
from locations_selectable import selectable_locations_list as locations_list
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = "SuperSecretKey" # Secret Key required for session["place"] to store info

@app.route('/',methods=['POST','GET'])
def index():
    if request.method =='POST':
        session["start"] = request.form["start"]
        session["finish"] = request.form["finish"]
        return redirect(url_for("directions"))
    else:
        return render_template("index.html")

@app.route("/directions")
def directions():
    try:
        text = babo_direct(session["start"],session["finish"])
        return render_template("directions.html", text = text)
    except:
        return render_template('error.html')