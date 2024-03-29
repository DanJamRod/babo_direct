import networkx as nx

def babson_graph():
    """ Creates graph in networkx, adds non-directional edges to it, and then returns the graph. 
        Weight is time in seconds between the nodes.
        One real-life roads may be represented by multiple nodes, e.g. path_map_hill_1 and path_map_hill_2.
        Map can be viewed at map.png
    """
    G = nx.Graph()
    G.add_edge("skating_lot", "skating_rink", weight = 30)
    G.add_edge("skating_rink", "bsc", weight = 30)
    G.add_edge("bsc", "path_fields_side", weight = 30)
    G.add_edge("path_fields_side", "becc", weight = 120)
    G.add_edge("path_fields_bryant", "macdowell_field", weight = 45)
    G.add_edge("path_fields_bryant", "hartwell_rogers_field", weight = 45)
    G.add_edge("path_fields_seating", "macdowell_field", weight = 45)
    G.add_edge("path_fields_seating", "hartwell_rogers_field", weight = 45)
    G.add_edge("path_fields_seating", "isbrandtsen_field", weight = 45)
    G.add_edge("path_fields_seating", "softball_field", weight = 45)
    G.add_edge("path_fields_seating", "path_fields_bryant", weight = 60)
    G.add_edge("path_fields_seating", "path_vw_hill_top", weight = 60)
    G.add_edge("path_vw_hill_top", "isbrandtsen_field", weight = 45)
    G.add_edge("path_vw_hill_top", "softball_field", weight = 45)
    G.add_edge("path_fields_side", "path_vw_hill_top", weight = 45)
    G.add_edge("path_fields_side", "tennis_court", weight = 45)
    G.add_edge("path_vw_hill_top", "van_winkle", weight = 30)
    G.add_edge("tennis_court", "coleman_lot", weight = 60)
    G.add_edge("coleman_lot", "van_winkle", weight = 45)
    G.add_edge("path_vw_hill_top", "coleman", weight = 45)
    G.add_edge("van_winkle", "coleman", weight = 30)
    G.add_edge("coleman", "path_map_hill_1", weight = 30)
    G.add_edge("van_winkle", "path_map_hill_1", weight = 75)
    G.add_edge("coleman_lot", "coleman", weight = 60)
    G.add_edge("coleman_lot", "path_map_hill_1", weight = 45)
    G.add_edge("path_map_hill_1", "path_map_hill_2", weight = 75)
    G.add_edge("coleman_lot", "path_map_hill_2", weight = 60)
    G.add_edge("path_map_hill_1", "path_pietz_mccullough", weight = 60)
    G.add_edge("path_vw_hill_top", "path_vw_hill_bottom", weight = 120)
    G.add_edge("path_pietz_mccullough", "mccullough", weight = 45)
    G.add_edge("mccullough", "path_map_hill_2", weight = 60)
    G.add_edge("mccullough", "putney", weight = 45)
    G.add_edge("putney", "mandell", weight = 45)
    G.add_edge("path_map_hill_2", "path_map_hill_3", weight = 120)
    G.add_edge("mandell", "path_map_hill_3", weight = 90)
    G.add_edge("path_map_hill_3", "trim_lot", weight = 45)
    G.add_edge("path_map_hill_3", "foundry", weight = 30)
    G.add_edge("foundry", "foundry_lot", weight = 30)
    G.add_edge("foundry_lot", "hollister_lot", weight = 30)
    G.add_edge("path_map_hill_3", "path_map_hill_4", weight = 75)
    G.add_edge("foundry_lot", "path_keith_canfield", weight = 90)
    G.add_edge("path_keith_canfield", "keith", weight = 15)
    G.add_edge("path_keith_canfield", "canfield", weight = 15)
    G.add_edge("path_keith_canfield", "pietz", weight = 30)
    G.add_edge("path_keith_canfield", "path_pietz_mccullough", weight = 45)
    G.add_edge("path_pietz_mccullough", "keith", weight = 45)
    G.add_edge("path_pietz_mccullough", "pietz", weight = 30)
    G.add_edge("path_vw_hill_bottom", "chapel", weight = 30)
    G.add_edge("chapel", "kriebel", weight = 30)
    G.add_edge("chapel", "sorenson", weight = 45)
    G.add_edge("sorenson", "reynolds", weight = 15)
    G.add_edge("sorenson", "path_vw_hill_bottom", weight = 30)
    G.add_edge("canfield", "reynolds", weight = 30)
    G.add_edge("path_reynolds_canfield", "canfield", weight = 30)
    G.add_edge("path_reynolds_canfield", "reynolds", weight = 30)
    G.add_edge("path_reynolds_canfield", "hollister_lot", weight = 30)
    G.add_edge("hollister_lot", "path_map_hill_4", weight = 15)
    G.add_edge("hollister", "path_map_hill_4", weight = 15)
    G.add_edge("path_map_hill_4", "trim", weight = 30)
    G.add_edge("trim", "rogers", weight = 30)
    G.add_edge("path_sullivan", "rogers", weight = 60)
    G.add_edge("path_sullivan", "forest", weight = 15)
    G.add_edge("path_sullivan", "public_safety", weight = 15)
    G.add_edge("public_safety", "sullivan", weight = 30)
    G.add_edge("sullivan", "sullivan_lot", weight = 30)
    G.add_edge("sullivan", "central_services", weight = 30)
    G.add_edge("central_services", "sullivan_lot", weight = 30)
    G.add_edge("sullivan_lot", "forest_annex", weight = 15)
    G.add_edge("forest", "forest_lot", weight = 30)
    G.add_edge("forest_lot", "path_sullivan", weight = 30)
    G.add_edge("path_sullivan", "path_college_1", weight = 30)
    G.add_edge("path_college_1", "path_college_2", weight = 60)
    G.add_edge("path_college_2", "path_college_3", weight = 45)
    G.add_edge("path_college_1", "rogers", weight = 30)
    G.add_edge("path_map_hill_4", "path_college_1", weight = 30)
    G.add_edge("path_college_3", "sorenson", weight = 15)
    G.add_edge("path_college_3", "reynolds", weight = 15)
    G.add_edge("path_college_3", "globe", weight = 15)
    G.add_edge("path_college_3", "path_college_4", weight = 60)
    G.add_edge("globe", "path_manor_way_1", weight = 15)
    G.add_edge("path_college_1", "path_nichols_1", weight = 45)
    G.add_edge("path_nichols_1", "nichols_lot", weight = 15)
    G.add_edge("path_nichols_1", "path_nichols_2", weight = 30)
    G.add_edge("path_nichols_2", "nichols", weight = 30)
    G.add_edge("path_nichols_2", "cruikshank", weight = 30)
    G.add_edge("path_nichols_2", "path_manor_way_3", weight = 30)
    G.add_edge("path_manor_way_3", "cruikshank", weight = 15)
    G.add_edge("path_manor_way_3", "millea", weight = 30)
    G.add_edge("path_manor_way_3", "post_office", weight = 45)
    G.add_edge("path_manor_way_3", "manor_north", weight = 45)
    G.add_edge("path_manor_way_3", "path_manor_way_2",weight = 15 )
    G.add_edge("path_manor_way_2", "nichols", weight = 30)
    G.add_edge("path_manor_way_1", "manor_south", weight = 15)
    G.add_edge("path_manor_way_2", "manor_south", weight = 15)
    G.add_edge("path_manor_way_2", "manor_quad", weight = 30)
    G.add_edge("manor_quad", "manor_south", weight = 30)
    G.add_edge("manor_quad", "manor_north", weight = 30)
    G.add_edge("manor_quad", "manor_west", weight = 30)
    G.add_edge("manor_west", "innovation", weight = 15)
    G.add_edge("manor_quad", "manor_central", weight = 30)
    G.add_edge("manor_quad", "tomasso", weight = 60)
    G.add_edge("manor_south", "path_college_4", weight = 30)
    G.add_edge("path_college_4", "commons", weight = 15)
    G.add_edge("path_college_4", "path_college_5", weight = 45)
    G.add_edge("manor_north", "mattos", weight = 45)
    G.add_edge("mattos", "tomasso", weight = 45)
    G.add_edge("tomasso", "path_tomasso_lawn", weight = 30)
    G.add_edge("path_tomasso_lawn", "luksic", weight = 30)
    G.add_edge("path_tomasso_lawn", "blank", weight = 30)
    G.add_edge("tomasso", "path_mustard_blank", weight = 30)
    G.add_edge("path_mustard_blank", "mustard", weight = 30)
    G.add_edge("path_mustard_blank", "blank", weight = 30)
    G.add_edge("mustard", "olin_lot", weight = 30)
    G.add_edge("olin_lot", "blank", weight = 30)
    G.add_edge("blank", "luksic", weight = 15)
    G.add_edge("luksic", "olin", weight = 45)
    G.add_edge("olin_lot", "olin", weight = 30)
    G.add_edge("path_tomasso_lawn", "path_college_5", weight = 30)
    G.add_edge("kriebel", "gerber", weight = 30)
    G.add_edge("gerber", "horn", weight = 15)
    G.add_edge("horn", "horn_cpu", weight = 30)
    G.add_edge("horn", "commons", weight = 15)
    G.add_edge("horn", "babson_hall", weight = 15)
    G.add_edge("babson_hall", "babson_lot", weight = 30)
    G.add_edge("babson_lot", "path_college_5", weight = 15)
    G.add_edge("path_college_5", "path_college_6", weight = 30)
    G.add_edge("path_college_6", "path_webster_stairs", weight = 45)
    G.add_edge("path_webster_stairs", "horn_cpu", weight = 45)
    G.add_edge("path_webster_stairs", "webster", weight = 30)
    G.add_edge("path_college_6", "olin", weight = 15)
    G.add_edge("path_college_6", "path_college_7", weight = 15)
    G.add_edge("olin", "path_olin_knight", weight = 15)
    G.add_edge("path_olin_knight", "knight_lot", weight = 45)
    G.add_edge("olin", "malloy", weight = 45)
    G.add_edge("malloy", "knight", weight = 15)
    G.add_edge("malloy", "knight_lot", weight = 30)
    G.add_edge("path_college_7", "malloy", weight = 15)
    G.add_edge("path_college_7", "brac", weight = 30)
    G.add_edge("path_college_7", "path_college_8", weight = 60)
    G.add_edge("webster", "webster_lot", weight = 30)
    G.add_edge("brac", "webster_lot", weight = 30)
    G.add_edge("webster_lot", "path_fields_bryant", weight = 30)
    G.add_edge("path_fields_bryant", "becc_lot", weight = 45)
    G.add_edge("becc_lot", "woodside", weight = 45)
    G.add_edge("woodside", "woodside_lot", weight = 30)
    G.add_edge("path_college_8", "bryant", weight = 30)
    G.add_edge("bryant", "path_babson_way_1", weight = 30)
    G.add_edge("bryant", "knight_lot", weight = 45)
    G.add_edge("knight_lot", "path_babson_way_1", weight = 45)
    G.add_edge("path_babson_way_1", "westgate", weight = 30)
    G.add_edge("westgate", "bryant_lot", weight = 45)
    G.add_edge("bryant", "bryant_lot", weight = 45)
    G.add_edge("path_college_8", "path_bryant_way", weight = 30)
    G.add_edge("path_bryant_way", "path_babson_way_2", weight = 30)
    G.add_edge("path_bryant_way", "webster_lot", weight = 30)
    G.add_edge("path_college_8", "path_babson_way_2", weight = 30)
    G.add_edge("path_babson_way_2", "bryant_lot", weight = 30)
    G.add_edge("woodside_lot", "path_babson_way_2", weight = 30)
    G.add_edge("path_babson_way_2", "path_babson_way_3", weight = 120)
    G.add_edge("path_babson_way_3", "woodland_lot", weight = 30)
    G.add_edge("path_babson_way_3", "woodland_1", weight = 30)
    G.add_edge("path_babson_way_3", "woodland_9", weight = 15)
    G.add_edge("woodland_1", "woodland_2", weight = 30)
    G.add_edge("woodland_2", "woodland_2a", weight = 30)
    G.add_edge("woodland_2a", "woodland_10", weight = 30)
    G.add_edge("woodland_10", "woodland_9", weight = 15)
    G.add_edge("woodland_2a", "woodland_3", weight = 30)
    G.add_edge("woodland_3", "woodland_4", weight = 30)
    G.add_edge("woodland_4", "woodland_5", weight = 15)
    G.add_edge("woodland_4", "woodland_6", weight = 30)
    G.add_edge("woodland_5", "woodland_7", weight = 30)
    G.add_edge("woodland_6", "woodland_7", weight = 15)
    G.add_edge("woodland_6", "woodland_8", weight = 30)
    G.add_edge("woodland_7", "woodland_8", weight = 30)
    G.add_edge("woodland_8", "woodland_lot", weight = 60) 
    return G

def route(start, finish):
    """ Calculates fastest route between a start and end node in a graph,
    returns the nodes passes, and appended on the end is the time taken in minutes.
    """
    G = babson_graph()
    directions = nx.shortest_path(G, source=start, target=finish, weight='weight', method='dijkstra')
    directions.append((nx.shortest_path_length(G, source=start, target=finish, weight='weight', method='dijkstra'))//60 + 1) # //60+1 translates the minutes into seconds, then rounds up
    return directions