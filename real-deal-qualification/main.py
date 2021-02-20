#!/usr/bin/env python3

from pprint import pprint
import locale
import random
import importlib
import sys
from decimal import Decimal
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

path = sys.argv[1]
heuristic = sys.argv[2]

def main():
    data = parse_input(path)
    module = importlib.import_module(heuristic)
    output = module.solve(data)

    outputify(output)
    print(f"{score(data, output):,}")

def outputify(output):
   name = path.split('/')[-1]
   with open("output/" + name, "w") as f:
       f.write(output)

def parse_input(path):
    with open(path) as f:
        i1, i2, i3 = [int(x) for x in f.readline().strip().split(" ")]

        data = []
        for line in f:
            data.append(set(line.strip().split(" ")[1:]))
    return pizzas
            
def score(data, string):
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
