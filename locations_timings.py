locations_timings = [
    ("skating_lot", "skating_rink", 30),
    ("staking_rink", "bsc", 30),
    ("path_fields_side", "beec", 120),
    ("beec", "path_fields_bryant", 45),
    ("path_fields_bryant", "macdowell_field", 45),
    ("path_fields_bryant", "hartwell_rogers_field", 45),
    ("path_fields_seating", "macdowell_field", 45),
    ("path_fields_seating", "hartwell_rogers_field", 45),
    ("path_fields_seating", "isbrandtsen_field", 45),
    ("path_fields_seating", "softball_field", 45),
    ("path_fields_seating", "path_fields_bryant", 60),
    ("path_fields_seating", "path_vw_hill_top", 60),
    ("path_vw_hill_top", "isbrandtsen_field", 45),
    ("path_vw_hill_top", "softball_field", 45),
    ("path_fields_side", "path_vw_hill_top", 45),
    ("path_fields_side", "tennis_court", 45),
    ("path_vw_hill_top", "van_winkle", 30),
    ("tennis_court", "coleman_lot", 60),
    ("coleman_lot", "van_winkle", 45),
    ("path_vw_hill_top", "coleman", 45),
    ("van_winkle", "coleman", 30),
    ("coleman", "path_map_hill_1", 30),
    ("van_winkle", "path_map_hill_1", 75),
    ("coleman_lot", "coleman", 60),
    ("coleman_lot", "path_map_hill_1", 45),
    ("path_map_hill_1", "path_map_hill_2", 75),
    ("coleman_lot", "path_map_hill_2", 60),
    #TBC
]

def locations():
    locations = []
    for tuple in locations_timings:
        if tuple[0] not in locations:
            locations.append(tuple[0])
        if tuple[1] not in locations:
            locations.append(tuple[1])
    return sorted(locations)

def main():
    print(locations())

if __name__ == "__main__":
    main()