from utils import *
from collections import Counter
print = logger.info

def solve(D, I, S, streets, car_paths):
    res= []
    intersections = {k: list() for k in range(I)}

    for street in streets:
        intersections[street[1]].append(street[2])

    prio_streets_counter = Counter({})
    for p in car_paths:
        first_street = p[1:][0]
        prio_streets_counter[first_street] += 1
    prio_streets = [ k for (k, v) in prio_streets_counter.most_common() ]

    all_streets_counter = Counter({})
    for p in car_paths:
        for s in p[1:]:
            all_streets_counter[s] += 1
    all_streets = [ k for (k, v) in all_streets_counter.most_common() ]

    res.append(str(I))
    for intersection, istreets in intersections.items():
        if not istreets:
            continue
        new_istreets = sorted(
            istreets,
            key = lambda x: prio_streets.index(x) if x in prio_streets else 99999999999
        )
        res.append(str(intersection))
        res.append(str(len(new_istreets)))
        for istreet in new_istreets:
            # res.append(f"{istreet} 1")
            c = prio_streets_counter[istreet] if istreet in prio_streets_counter else 1
            res.append(f"{istreet} {max(1, c)}")
            # c = all_streets_counter[istreet] if istreet in all_streets_counter else 1
            # res.append(f"{istreet} {max(1, c//5)}")
    return "\n".join(res)

@timer
def helper():
    return "bro"
