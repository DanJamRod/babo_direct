from dijkstra import route as route
from locations_name import locations_dict as locations_name

def directions(start, finish):
    """ Returns a list of directions from the list of nodes
    """
    name = locations_name()
    directions = []
    path = route(start, finish)
    directions.append(f"Leave {name[start]}")
    for i in range(len(path)-3): # Exludes the weight at the end, and the first and last node
        if path[i+1][:4] == "path" and name[path[i+1]] != name[path[i+2]]:
            directions.append(f"Walk along {name[path[i+1]]}")
        elif path[i+1][:4] != "path": 
            directions.append(f"Walk past {name[path[i+1]]}")
    directions.append(f"You are at {name[finish]}!")
    directions.append(path[-1]) # Adds on the time taken in minutes to the list of directions
    return directions