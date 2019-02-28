import os
import csv
import pprint

# with open(os.path.dirname(os.path.abspath(__file__)) + '/buzzers.csv') as raw_data:
#     print(raw_data.read())

# with open(os.path.dirname(os.path.abspath(__file__)) + '/buzzers.csv') as data:
#     for line in csv.reader(data):
#         print(line)

# with open(os.path.dirname(os.path.abspath(__file__)) + '/buzzers.csv') as data:
#     for line in csv.DictReader(data):
#         print(line)

with open(os.path.dirname(os.path.abspath(__file__)) + '/buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v
    pprint.pprint(flights)
