#!/usr/bin/env python3

from pprint import pprint
import locale
import random
import sys
from decimal import Decimal

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

two, three, four = [0, 0 , 0]
path = sys.argv[1]

def f(d):
   return '{0:n}'.format(d)

def main():
    pizza = parse_input(path)
    output = attempt3(pizza)
    #pprint(pizza)
    #print(output)
    #print(locale.format(score(pizza, output)))
    print(f"{score(pizza, output):,}")
    #print(locale.format_string("%d", score(pizza, output), grouping=True))

    outputify(output)

def outputify(output):
   name = path.split('/')[-1]
   with open("output/" + name, "w") as f:
       f.write(output)

def attempt1(pizza):
    "Largest teams first, first pizza first :D"
    teams = [4]*four+[3]*three+[2]*two
    pizza_idx = 0
    output = []
    for t in teams:
        if pizza_idx + t > len(pizza):
            continue
        output.append(f'{t} ' + " ".join([str(x) for x in range(pizza_idx, pizza_idx+t)]))
        pizza_idx += t
    return f"{len(output)}\n" + "\n".join(output)

def attempt2(pizza):
    "Smallest team first, first pizza first :D"
    teams = [2]*two+[3]*three+[4]*four
    pizza_idx = 0
    output = []
    for t in teams:
        if pizza_idx + t > len(pizza):
            continue
        output.append(f'{t} ' + " ".join([str(x) for x in range(pizza_idx, pizza_idx+t)]))
        pizza_idx += t
    return f"{len(output)}\n" + "\n".join(output)

def attempt3(pizzas):
    pizza_idxs = [x[0] for x in enumerate(pizzas)]
    sorted_pizza_idx = sorted(pizza_idxs, key=lambda i: len(pizzas[i]), reverse=False)

    teams = [4]*four+[3]*three+[2]*two
    pizza_idx = 0
    output = []
    for t in teams:
        if pizza_idx + t > len(pizzas):
            continue
        output.append(f'{t} ' + " ".join([str(sorted_pizza_idx[x]) for x in range(pizza_idx, pizza_idx+t)]))
        pizza_idx += t

    return f"{len(output)}\n" + "\n".join(output)

def parse_input(path):
    global two, three, four
    with open(path) as f:
        pizza_count, two, three, four = [int(x) for x in f.readline().strip().split(" ")]

        pizzas = []
        for line in f:
            pizzas.append(set(line.strip().split(" ")[1:]))
    return pizzas
            
def score(pizza, string):
    lines = string.split("\n")
    rows = int(lines[0])
    lines = [x for x in lines[1:] if x]

    intermediate_score = 0
    for line in lines:
        unique = set([xx for x in line.strip().split(" ")[1:]
                for xx in pizza[int(x)]])
        intermediate_score+=len(unique)**2
    return intermediate_score

main()
