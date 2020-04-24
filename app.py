# export FLASK_APP=app.py && python3 -m flask run

from directions import directions as directions
from locations_selectable import selectable_locations_dict as locations_dict
from locations_selectable import selectable_locations_list as locations_list
from flask import Flask

# # Users need to see locations_dict.values() i.e. locations_list, but locations_dict.keys() has to be inputted to the algorithm
# locations_dict = locations_dict()
# locations_list = locations_list()
# print(locations_dict)
# print(f"\n\n")
# print(locations_list)

app = Flask(__name__)