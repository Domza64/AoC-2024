grid = []
all_antinodes = set()
antennas = {}


def within_bounds(antinode_pos):
    return 0 <= antinode_pos[0] < (len(grid[0])) and 0 <= antinode_pos[1] < (len(grid))


def get_antinodes(point_1, point_2):
    antinodes = []

    x1, x2 = point_1[0], point_2[0]
    y1, y2 = point_1[1], point_2[1]
    x_distance = abs(x1 - x2)
    y_distance = abs(y1 - y2)

    if (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2):
        antinode_1 = (min(x1, x2) - x_distance, min(y1, y2) - y_distance)
        antinode_2 = (max(x1, x2) + x_distance, max(y1, y2) + y_distance)
    else:
        antinode_1 = (min(x1, x2) - x_distance, max(y1, y2) + y_distance)
        antinode_2 = (max(x1, x2) + x_distance, min(y1, y2) - y_distance)

    if within_bounds(antinode_1):
        antinodes.append(antinode_1)
    if within_bounds(antinode_2):
        antinodes.append(antinode_2)
    return antinodes


with open('input.txt', 'r') as file:
    y = 0
    for line in file:
        x = 0
        grid.append([])
        for char in line.strip():
            if char != ".":
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
            grid[y].append(char)
            x += 1
        y += 1


def field_empty(pos, current_antenna):
    char_on_field = grid[pos[1]][pos[0]]
    if char_on_field != current_antenna:
        return True
    return False


for key in antennas:
    for antenna_1 in antennas[key]:
        for antenna_2 in antennas[key]:
            if antenna_1 != antenna_2:
                for antinode in get_antinodes(antenna_1, antenna_2):
                    if field_empty(antinode, key):
                        all_antinodes.add(antinode)

print("Part 1:", len(all_antinodes))

