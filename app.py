# export FLASK_APP=app.py && python3 -m flask run

from directions import directions as directions
from locations_name import locations as locations
from flask import Flask

# print(locations())

app = Flask(__name__)