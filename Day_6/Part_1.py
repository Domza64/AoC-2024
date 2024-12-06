map_grid = []
pos = (0, 0)
directions = "nesw"
direction = "n"

with open('input.txt', 'r') as file:
    y = 0
    for line in file:
        if "^" in line:
            pos = (line.find("^"), y)
            line = line.replace("^", "X")
        map_grid.append(list(line.strip()))
        y += 1

while True:
    new_pos = (0, 0)
    if direction == "n":
        new_pos = (pos[0], pos[1] - 1)
    elif direction == "e":
        new_pos = (pos[0] + 1, pos[1])
    elif direction == "s":
        new_pos = (pos[0], pos[1] + 1)
    elif direction == "w":
        new_pos = (pos[0] - 1, pos[1])

    if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] > len(map_grid[0]) - 1 or new_pos[1] > len(map_grid) - 1:
        break

    current_field = map_grid[new_pos[1]][new_pos[0]]
    if current_field == "." or current_field == "X":
        map_grid[new_pos[1]][new_pos[0]] = "X"
        pos = new_pos
    elif current_field == "#":
        new_direction_val = directions.find(direction) + 1
        if new_direction_val == 4:
            new_direction_val = 0
        direction = directions[new_direction_val]

locations_sum = 0
for line in map_grid:
    locations_sum += line.count("X")

print(locations_sum)
