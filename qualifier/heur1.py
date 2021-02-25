from utils import *
print = logger.info

def solve(D, I, S, streets, car_paths):
    res= []
    intersections = {k: list() for k in range(I)}

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
            print(f"{istreet} 1")
            res.append(f"{istreet} 1")
    return "\n".join(res)

@timer
def helper():
    return "bro"
