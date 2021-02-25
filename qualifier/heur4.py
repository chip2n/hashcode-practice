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

    num_intersections = 0
    for intersection, istreets in intersections.items():
        if not istreets:
            continue

        intersection_counts = [ counter[istreet] for istreet in istreets ]
        total = sum(intersection_counts)
        if not total:
            continue

        output_streets = []
        max_count = max(intersection_counts)
        for istreet in istreets:
            if counter[istreet] / max_count < 0.1:
                continue
            count = max(1, int((counter[istreet] / total) * 2 * len(istreets)))

            output_streets.append(f"{istreet} {count}")
        if output_streets:
            num_intersections += 1
            res.append(str(intersection))
            res.append(str(len(output_streets)))
            res += output_streets
    return "\n".join([str(num_intersections)] + res)

@timer
def helper():
    return "bro"
