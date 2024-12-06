# This is actually funny...,
# Running this AMAZING algo on my trusty ThinkPad T560 only took 2 minutes and 25 seconds
# to find a solution for this challenge. Hope my future boss don't see this :>

# As they say, if it works don't touch it!

import copy

map_grid = []
start_pos = (0, 0)
with open('input.txt', 'r') as file:
    y = 0
    for line in file:
        if "^" in line:
            start_pos = (line.find("^"), y)
        map_grid.append(list(line.strip()))
        y += 1


def is_infinite(grid):
    all_positions_count = len(grid[0]) * len(grid)
    pos = start_pos
    directions = "nesw"
    direction = "n"
    all_positions = []
    while True:
        if all_positions_count < len(all_positions):
            return True

        new_pos = (0, 0)
        if direction == "n":
            new_pos = (pos[0], pos[1] - 1)
        elif direction == "e":
            new_pos = (pos[0] + 1, pos[1])
        elif direction == "s":
            new_pos = (pos[0], pos[1] + 1)
        elif direction == "w":
            new_pos = (pos[0] - 1, pos[1])

        if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] > len(grid[0]) - 1 or new_pos[1] > len(grid) - 1:
            return False

        current_field = grid[new_pos[1]][new_pos[0]]
        if current_field == "#":
            new_direction_val = directions.find(direction) + 1
            if new_direction_val == 4:
                new_direction_val = 0
            direction = directions[new_direction_val]
            continue
        else:
            all_positions.append(new_pos)
            pos = new_pos


counter = 1
possible_infinite = 0
possibilities = len(map_grid[0]) * len(map_grid)
for i in range(len(map_grid)):
    for j in range(len(map_grid[0])):
        print("Progress:", counter, "of:", possibilities)
        counter += 1
        new_grid = copy.deepcopy(map_grid)
        if new_grid[i][j] != ".":
            continue
        new_grid[i][j] = "#"
        if is_infinite(new_grid):
            possible_infinite += 1

print(possible_infinite)
