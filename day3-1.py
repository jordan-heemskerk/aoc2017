import math


target = 289326


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

print coord
print abs(coord[0]) + abs(coord[1])

