# python 3.py < 3.txt
from collections import defaultdict

with open(0) as file:
    data = file.readlines()

claims = []
for index, line in enumerate(data):
    split = line.split()
    corner = split[2][:-1].split(',')
    x, y = int(corner[0]), int(corner[1])
    dimensions = split[3].split('x')
    dx, dy = int(dimensions[0]), int(dimensions[1])
    claim = (index + 1, (x, y, x+dx-1, y+dy-1))
    claims.append(claim)

# ids of claims that have cover a position
# key = (x, y)
# value = set of claims covering that position
claimed = defaultdict(set)

# ids of claims that have no overlap with any other claim
no_overlap = set(range(1, len(claims)+1))

result_1 = 0 # no. of positions covered by > 1 claim
for (id_, (x0, y0, x1, y1)) in claims:
    for ix in range(x0, x1+1):
        for iy in range(y0, y1+1):
            position = (ix, iy)
            if position in claimed and len(claimed[position]) == 1:
                result_1 += 1
            claimed[position].add(id_)
            if len(claimed[position]) > 1:
                for claim in claimed[position]:
                    if claim in no_overlap:
                        no_overlap.remove(claim)

print(result_1, no_overlap)
