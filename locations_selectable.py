from locations_name import locations_dict as locations

def all_locations_dict():
    """ Returns the locations dictionary from locations_name.
    """
    all_locations_dict = locations()
    return all_locations_dict

def selectable_locations_dict():
    """ Returns the locations dictionary from locations_name,
        excluding the values that are a path.
        (Will be the locations that the user can select)
    """
    selectable_locations_dict = locations()
    paths = []
    for location in selectable_locations_dict:
        if location[:4] == "path": # All of the path locations begin with "path_...""
            paths.append(location)
    for path in paths:
        del selectable_locations_dict[path]
    return selectable_locations_dict

def all_locations_list():
    """ Returns a list of all locations (the values from the all_locations_dict)
    """
    all_locations = all_locations_dict()
    all_locations_list = []
    for location in all_locations:
        all_locations_list.append(all_locations[location])
    return all_locations_list

def selectable_locations_list():
    """ Returns a list of all non-path locations (the values from the selectable_locations_dict)
    """
    selectable_locations = selectable_locations_dict()
    selectable_locations_list = []
    for location in selectable_locations:
        selectable_locations_list.append(selectable_locations[location])
    return selectable_locations_list

def main():
    print(f"All Locations:\n{all_locations_list()}\n\n")
    print(f"Selectable Locations:\n{selectable_locations_list()}")

if __name__ == '__main__':
    main()
