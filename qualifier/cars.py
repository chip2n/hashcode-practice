#!/usr/bin/env python3

D = 6
I = 4
S = 5
V = 2
F = 1000

streets = [
    (2, 0, 'rue-de-londers', 1),
    (0, 1, 'rue-d-amsterdam', 1),
    (3, 1, 'rue-d-athenes', 1),
    (2, 3, 'rue-de-rome', 2),
    (1, 2, 'rue-de-moscou', 3),
]

car_paths = [
    (4, 'rue-de-londres', 'rue-d-amsterdam', 'rue-de-moscou', 'rue-de-rome'),
    (3, 'rue-d-athenes', 'rue-de-moscou', 'rue-de-londres'),
]

print(streets)
print(car_paths)


intersections = {k: list() for k in range(I)}

for street in streets:
    intersections[street[0]].append(street[2])

print(intersections)

print(I)
for intersection, istreets in intersections.items():
    print(intersection)
    print(len(istreets))
    for istreet in istreets:
        print(istreet, 1)
