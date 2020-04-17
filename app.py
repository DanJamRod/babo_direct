# export FLASK_APP=app.py && python3 -m flask run

from directions.directions import main as directions
from flask import Flask

app = Flask(__name__)