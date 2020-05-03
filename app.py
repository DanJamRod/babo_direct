from directions import directions as babo_direct
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = "SuperSecretKey" # Secret Key required for session["start"] to store info

@app.route('/',methods=['POST','GET'])
def index():
    """ Index/home page. Take inputs of start/end location, and then directs to directions.html
    """
    if request.method =='POST':
        session["start"] = request.form["start"]
        session["finish"] = request.form["finish"]
        return redirect(url_for("directions"))
    else:
        return render_template("index.html")

@app.route("/directions")
def directions():
    """ Displays directions, uses imported directions function. If any errors, it displays an error page
    """
    try:
        text = babo_direct(session["start"],session["finish"])
        return render_template("directions.html", \
        text = text[:-1], time = text[-1], start = session["start"], finish = session["finish"])  # Last item in list is time taken, see directions.py 
    except:
        return render_template('error.html')