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

    special_counter = { k: v for k, v in counter.items() if '-ejj' in k and v > 1}

    prio_streets_counter = Counter({})
    for p in car_paths:
        first_street = p[1:][0]
        if '-ejj' in first_street:
            prio_streets_counter[first_street] += 1
    prio_streets = [ k for (k, v) in prio_streets_counter.most_common() ]

    for street in streets:
        intersections[street[1]].append(street[2])

    num_intersections = 0
    for intersection, istreets in intersections.items():
        new_istreets = [ s for s in istreets if s in special_counter]
        new_istreets.sort(
            key = lambda x: prio_streets.index(x) if x in prio_streets else 99999999999
        )
        if intersection == 499:
            num_intersections += 1
            res.append(str(intersection))
            res.append(str(len(new_istreets)))
            for istreet in new_istreets:
                c = prio_streets_counter[istreet] if istreet in prio_streets_counter else 1
                res.append(f"{istreet} {max(1, c//2)}")
            continue

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
