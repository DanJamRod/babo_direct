from locations_name import locations_dict as locations

def all_locations_dict():
    all_locations_dict = locations()
    return all_locations_dict

def selectable_locations_dict():
    selectable_locations_dict = locations()
    paths = []
    for location in selectable_locations_dict:
        if location[:4] == "path":
            paths.append(location)
    for path in paths:
        del selectable_locations_dict[path]
    return selectable_locations_dict

def all_locations_list():
    all_locations = all_locations_dict()
    all_locations_list = []
    for location in all_locations:
        all_locations_list.append(all_locations[location])
    return all_locations_list

def selectable_locations_list():
    selectable_locations = selectable_locations_dict()
    selectable_locations_list = []
    for location in selectable_locations:
        selectable_locations_list.append(selectable_locations[location])
    return selectable_locations_list

def translate(location):
    selectable_locations = selectable_locations_dict()
    translate_locations = dict([(value, key) for key, value in selectable_locations.items()])
    return translate_locations[location]

def main():
    print(f"All Locations:\n{all_locations_list()}\n\n")
    print(f"Selectable Locations:\n{selectable_locations_list()}")

if __name__ == '__main__':
    main()
