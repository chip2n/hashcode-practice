from utils import *
from collections import Counter
print = logger.info

def solve(D, I, S, streets, car_paths):
    """Give each street at least 1 second, but some gets more based on weight
    uses scale=2
    """
    res= []
    intersections = {k: list() for k in range(I)}

    counter = Counter({})
    for p in car_paths:
        for s in p[1:]:
            counter[s] += 1

    for street in streets:
        intersections[street[1]].append(street[2])

    # print(intersections)

    # print(I)
    # res.append(str(I))

    num_intersections = 0
    for intersection, istreets in intersections.items():
        if not istreets:
            continue

        total = sum(counter[istreet] for istreet in istreets)
        if not total:
            continue
        num_intersections += 1
        res.append(str(intersection))
        res.append(str(len(istreets)))
        for istreet in istreets:
            count = max(1, int((counter[istreet] / total) * 2 * len(istreets)))
            # print(f"{istreet} {count}")
            res.append(f"{istreet} {count}")
    return "\n".join([str(num_intersections)] + res)

@timer
def helper():
    return "bro"
