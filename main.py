#!/usr/bin/env python3

from pprint import pprint
import locale
import random
import sys
from decimal import Decimal

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

two, three, four = [0, 0 , 0]
path = sys.argv[1]

def main():
    pizza = parse_input(path)
    output = attempt5(pizza)

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

def attempt4greedy(pizzas):
    poke_bowls = {i: p for i, p in enumerate(pizzas)}
    def best_pizza_combo(pizza_count):
        selected = []
        ingredients = set()
        for _ in range(0, pizza_count):
            scored_bowls = [(len(p.difference(ingredients)), i, p) for i, p in poke_bowls.items()]
            best = max(scored_bowls)
            selected.append(best[1])
            ingredients |= best[2]
            del poke_bowls[best[1]]


        return selected

    teams = [4]*four+[3]*three+[2]*two
    output = []
    for count, t in enumerate(teams):
        if count % 100 == 0:
            print(f"count: {count}")
        if t > len(poke_bowls):
            continue
        selected = best_pizza_combo(t)
        output.append(f"{t} " + " ".join([str(s) for s in selected]))
    return f"{len(output)}\n" + "\n".join(output)

def attempt5(pizzas):
    sorted_pizzas = sorted(enumerate(pizzas), key=lambda x: len(x[1]), reverse=True)
    def best_pizza_combo(pizza_count):
        selected = []
        ingredients = set()
        for _ in range(0, pizza_count):
            best = (-1, None, None)
            for idx, p in enumerate(sorted_pizzas):
                if len(p[1]) < best[0]:
                    break
                score = len(p[1].difference(ingredients))
                if score >= best[0]:
                    best = (score, idx, p)
            selected.append(best[1])
            ingredients |= best[2][1]
            del sorted_pizzas[best[1]]
        return selected

    teams = [4]*four+[3]*three+[2]*two
    output = []
    for count, t in enumerate(teams):
        if count % 100 == 0:
            print(f"count: {count}")
        if t > len(sorted_pizzas):
            continue
        selected = best_pizza_combo(t)
        output.append(f"{t} " + " ".join([str(s) for s in selected]))
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
