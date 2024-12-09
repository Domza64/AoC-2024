grid = []
antennas = {}


def within_bounds(antinode_pos):
    return 0 <= antinode_pos[0] < len(grid[0]) and 0 <= antinode_pos[1] < len(grid)


def get_antinodes(point_1, point_2):
    found_antinodes = {point_1, point_2}
    x1, x2 = point_1[0], point_2[0]
    y1, y2 = point_1[1], point_2[1]
    distance_vector = (x1 - x2, y1 - y2)

    pos = point_2
    while within_bounds(pos):
        found_antinodes.add(pos)
        pos = (pos[0] + distance_vector[0], pos[1] + distance_vector[1])

    pos = point_1
    while within_bounds(pos):
        found_antinodes.add(pos)
        pos = (pos[0] - distance_vector[0], pos[1] - distance_vector[1])

    return found_antinodes


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

all_antinodes = set()
for key in antennas:
    for i in range(len(antennas[key])):
        for j in range(i + 1, len(antennas[key])):
            antinodes = get_antinodes(antennas[key][i], antennas[key][j])
            all_antinodes.update(antinodes)

print("Part 2:", len(all_antinodes))
