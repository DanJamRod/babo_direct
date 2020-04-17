from collections import defaultdict

class Graph():
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

graph = Graph()

edges = [
    ('Rogers Pub', 'the bottom of the Trim stairs', 1),
    ('the bottom of the Trim stairs', 'Trim', 1),
    ('Babson Drive A', 'the bottom of the Trim stairs', 1),
    ('Babson Drive A', 'Babson Hill A', 1),
    ('Babson Drive A', 'Babson Drive B', 1),
    ('Babson Hill A', 'Trim', 1),
    ('Babson Hill A', 'Babson Hill B', 1),
    ('Babson Hill A', 'Hollister side entrance', 1),
    ('Babson Hill B', 'Babson Hill C', 2),
    ('Babson Hill B', 'Hollister Lot', 1),
    ('Babson Hill C', 'the Innovation Center', 1),
    ('Babson Hill C', 'Trim Lot', 1),
    ('Babson Drive B', 'Babson Drive C', 2),
    ('Babson Drive B', 'Hollister front entrance', 1),
    ('Hollister front entrance', 'Reynolds front entrance', 2),
    ('Hollister', 'Hollister front entrance', 0),
    ('Hollister', 'Hollister side entrance', 0),
    ('Hollister Lot', 'Reynolds back entrance', 2),
    ('Hollister Lot', 'the Innovation Center', 2),
    ('the Globe', 'Babson Drive C', 1),
    ('Babson Drive C', 'Reynolds front entrance', 1),
    ('Babson Drive C', 'Babson Drive D', 1),
    ('Reynolds', 'Reynolds front entrance', 0),
    ('Reynolds', 'Reynolds back entrance', 0),
    ('Reynolds', 'Reynolds side entrance', 0),
    ('Reynolds front entrance', 'Sorenson front entrance', 1),
    ('Reynolds side entrance', 'Sorenson side entrance', 1),
    ('Reynolds side entrance', 'Reynolds back entrance', 1),
    ('Babson Drive D', 'Sorenson front entrance', 1),
    ('Sorenson', 'Sorenson front entrance', 0),
    ('Sorenson', 'Sorenson side entrance', 0),
]

for edge in edges:
    graph.add_edge(*edge)

def dijkstra(graph, initial, end):
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back entrance through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

def babo_direct(start, end):
    path = dijkstra(graph, start, end)
    print(f"\nDirections from {path[0]} to {path[-1]}")
    print("-"*(len(path[0])+len(path[-1])+20))
    if path[1][-8:] == "entrance":
        path = path[1:]
    print(f"Leave {path[0]}")
    for i in range (len(path)-3):
        if ord("A") <= ord(path[i+1][-1])  <= ord("Z") and path[i+1][:-3] != path[i+2][:-3]:
            print(f"Cross the {path[i+1][:-2]} road")
        elif ord("A") <= ord(path[i+1][-1])  <= ord("Z") and path[i+1][:-3] == path[i+2][:-3]:
            path[i+2] = path[i+1]
        elif ord("A") <= ord(path[i+1][-1])  <= ord("Z"):
            print(f"Walk along {path[i+1][:-2]}")          
        elif path[i+1][0:4] == path[i+2][0:4]:
            path[i+1] = path[i+2]
        elif path[i+1][-3:] == "Lot":
            print(f"Walk through {path[i+1]}")
        elif path[i+1][-13:] == "side entrance" or path[i+1][-13:] == "back entrance" :
            print(f"Walk around {path[i+1][:-13]}and past the {path[i+1][-13:]}")
        elif path[i+1][-14:] == "front entrance":
            print(f"Walk around {path[i+1][:-14]}and past the {path[i+1][-14:]}")
        else:    
            print(f"Walk past {path[i+1]}")
    if path[-2][-8:] == "entrance":
        print(f"Walk through the {path[-2]}")
    elif (path[-2][-6:-2] == "Hill" and path[-2][-6:-2] == "Hill") or (path[-2][-7:-2] == "Drive" and path[-2][-7:-2] == "Drive"):
        print(f"Walk along {path[-2][:-2]} until you see {path[-1]}")
    elif path[-2][-3:] == "Lot":
        print(f"Walk through {path[-2]} until you see {path[-1]}")
    else:
        print(f"Continue past {path[-2]} until you see {path[-1]}")
    print(f"You are at {path[-1]}!")