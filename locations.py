locations_selectable = {
    "test_no":0,
    "test_yes":1,
    "z":1,
    "a":1
}

def locations():
    return sorted(locations_selectable.keys())

def selectable_locations():
    selectable_locations = []
    for location in locations_selectable:
        if locations_selectable[location] == 1:
            selectable_locations.append(location)
    return sorted(selectable_locations)

def main():
    print(f"Locations: {locations()}")
    print(f"Selectable Locations: {selectable_locations()}")

if __name__ == '__main__':
    main()
