from utils import *
from collections import Counter
print = logger.info

def solve(D, I, S, streets, car_paths):
    res= []
    intersections = {k: list() for k in range(I)}

    counter = Counter({})
    for p in car_paths:
        for s in p[1:]:
            counter[s] += 1

    for street in streets:
        intersections[street[1]].append(street[2])

    print(intersections)

    print(I)
    res.append(str(I))
    for intersection, istreets in intersections.items():
        if not istreets:
            continue
        print(intersection)
        res.append(str(intersection))
        print(len(istreets))
        res.append(str(len(istreets)))
        for istreet in istreets:
            count = counter[istreet]
            print(f"{istreet} {count}")
            res.append(f"{istreet} {count}")
    return "\n".join(res)

@timer
def helper():
    return "bro"
