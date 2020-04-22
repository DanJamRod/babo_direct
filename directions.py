from dijsktra import route as route

def directions(start, finish):
    return route(start, finish)

def main():
    """ use for testing
    """
    print(directions("X", "Y"))

if __name__ == '__main__':
    main()