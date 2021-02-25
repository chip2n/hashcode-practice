#!/usr/bin/env python3

from pprint import pprint
import locale
import random
import importlib
import sys
from utils import *

from decimal import Decimal
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

import logging

path = sys.argv[1]
heuristic = sys.argv[2]
name = path.split('/')[-1]

print = logger.info
logging.basicConfig(format = f'{name} ({heuristic}): %(message)s')
logger.setLevel(logging.DEBUG)

def main():
    D, I, S, streets, car_paths = parse_input(path)
    module = importlib.import_module(heuristic)
    output = timer(module.solve)(streets)

    s = score(streets, car_paths, output)
    outputify(output, s)

def outputify(output, score):
    with open("output/" + name + "----" + str(f"{score:,}").rjust(14, '-') + "---" + heuristic, "w") as f:
        f.write(output)
    print(f"Score: {score:,}")

def parse_input(path):
    with open(path) as f:
        D, I, S, V, F = [int(x) for x in f.readline().strip().split(" ")]

        streets = []
        car_paths = []

        for _ in range(S):
            start, end, name, length = f.readline().strip().split(" ")
            streets.append((int(start), int(end), name, int(length)))
        for _ in range(V):
            car_data = f.readline().strip().split(" ")
            car_data[0] = int(car_data[0])
            car_paths.append(tuple(car_data))

    return D, I, S, transform_streets(streets), transform_car_paths(car_paths)

def transform_streets(streets):
    result = dict()
    for [start, end, name, street_no, length] in streets:
        result[name] = {
            "start_intersection": start,
            "end_intersection": end,
            "length": length,
        }
    return result

def transform_car_paths(paths):
    for p in paths:
        p = path[1:]
    return paths

def score(streets, car_paths, string):
    return 0
    lines = string.split("\n")
    rows = int(lines[0])
    lines = [x for x in lines[1:] if x]

    intermediate_score = 0
    for line in lines:
        unique = set([xx for x in line.strip().split(" ")[1:]
                for xx in data[int(x)]])
        intermediate_score+=len(unique)**2
    return intermediate_score


main()
