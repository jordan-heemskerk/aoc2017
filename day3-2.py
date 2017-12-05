import math
from collections import defaultdict

min_val = 289326

def linear_to_idxs(target):

    s_target = math.sqrt(target)

    # bound between perfect squares
    min_square = int(s_target)

    if min_square % 2 == 0:
        min_square -= 1

    max_square = min_square + 2

    ring = (max_square - 1) / 2

    bottom_right = (ring, -ring)

    
    if target > max_square**2 - (max_square - 1):
        #bottom
        diff = target - (max_square**2 - 1 * (max_square - 1))
        coord = (-ring + diff, -ring)    
    elif target > max_square**2 - 2 * (max_square - 1):
        #left
        diff = target - (max_square**2 - 2 * (max_square - 1))
        coord = (-ring, ring - diff)
    elif target > max_square**2 - 3 * (max_square - 1):
        diff = target - (max_square**2 - 3 * (max_square - 1))
        coord = (ring - diff, ring)
    elif target > max_square**2 - 4 * (max_square - 1):
        #left
        diff = target - (max_square**2 - 4 * (max_square - 1))
        coord = (ring, - ring + diff)
    else:
        coord = (ring - 1, -ring + 1)
    return coord


def generate_neighbours(idxs):
    yield idxs[0] + 1, idxs[1]
    yield idxs[0] + 1, idxs[1] + 1
    yield idxs[0] + 1, idxs[1] - 1
    yield idxs[0] - 1, idxs[1]
    yield idxs[0] - 1, idxs[1] + 1
    yield idxs[0] - 1, idxs[1] - 1
    yield idxs[0], idxs[1] + 1
    yield idxs[0], idxs[1] - 1

filled = defaultdict(lambda: 0)

filled[(0, 0)] = 1
for linear in range(2, min_val):
    x, y = linear_to_idxs(linear)
    fill_val = 0
    for n in generate_neighbours((x, y)):
        fill_val += filled[n]
    if fill_val > min_val:
        print fill_val
        break
    filled[(x, y)] = fill_val
     
