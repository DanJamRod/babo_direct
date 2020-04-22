locations_timings = [
    ('X', 'A', 7),
    ('X', 'B', 2),
    ('X', 'C', 3),
    ('X', 'E', 4),
    ('A', 'B', 3),
    ('A', 'D', 4),
    ('B', 'D', 4),
    ('B', 'H', 5),
    ('C', 'L', 2),
    ('D', 'F', 1),
    ('F', 'H', 3),
    ('G', 'H', 2),
    ('G', 'Y', 2),
    ('I', 'J', 6),
    ('I', 'K', 4),
    ('I', 'L', 4),
    ('J', 'L', 1),
    ('K', 'Y', 5),
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

if __name__ == '__main__':
    main()