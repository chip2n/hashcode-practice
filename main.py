#!/usr/bin/env python3
from pprint import pprint
import sys
two, three, four = [0, 0 , 0]
path = sys.argv[1]

def main():
    pizza = parse_input(path)
    output = naive_solution(pizza)
    pprint(pizza)
    print(output)
    print(score(output, path))

def naive_solution(pizza):
    teams = [4]*four+[3]*three+[2]*two
    pizza_idx = 0
    output = []
    for t in teams:
        if pizza_idx + t > len(pizza):
            continue
        output.append(f'{t} ' + " ".join([str(x) for x in range(pizza_idx, pizza_idx+t)]))
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
            
def score(string, path):
    pizza = parse_input(path)
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
