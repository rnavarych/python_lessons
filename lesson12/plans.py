from datetime import datetime
import pprint
import os


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open(os.path.dirname(os.path.abspath(__file__)) + '/buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

    pprint.pprint(flights)
    print()

    flights2 = {}
    for k,v in flights.items():
        flights2[convert2ampm(k)] = v.title()

    pprint.pprint(flights2)
    print()


with open(os.path.dirname(os.path.abspath(__file__)) + '/buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

    more_dests = [dest.title() for dest in flights.values()]
    more_flights = {convert2ampm(k): v.title() for k, v in flights.items()}

    pprint.pprint(more_dests)
    print()
    pprint.pprint(more_flights)

    dests = set(more_dests)
    print()
    pprint.pprint(dests)
    print()

    when = {}
    for dest in set(more_flights.values()):
        when[dest] = [k for k, v in more_flights.items() if v == dest]
    pprint.pprint(when)
    print()

    when2 = {dest: [k for k, v in more_flights.items() if v == dest] for dest in set(more_flights.values())}
    pprint.pprint(when2)
    print()
