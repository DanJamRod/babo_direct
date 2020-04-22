locations_name = {
    "test_no": "Test No",
    "test_yes": "Test Yes",
    "z": "Letter",
    "a": "Letter"
}

def locations():
    location_name = []
    for location in locations_name:
        if locations_name[location] not in location_name:
            location_name.append(locations_name[location])
    return sorted(location_name)

def main():
    print(locations())

if __name__ == '__main__':
    main()