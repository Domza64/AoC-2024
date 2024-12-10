def get_map():
    with open('input.txt', 'r') as file:
        map_data = []
        for index, line in enumerate(file):
            map_data.append([])
            line = line.strip()
            for char in line:
                map_data[index].append(char)
    return map_data


def get_trailheads(topographic_map):
    trail_heads = []
    for y, row in enumerate(topographic_map):
        for x, height_point in enumerate(row):
            if height_point == "0":
                trail_heads.append((x, y))
    return trail_heads


def get_height(pos, topographic_map):
    return topographic_map[pos[1]][pos[0]]


def within_bounds(pos, topographic_map):
    x = pos[0]
    y = pos[1]
    return 0 <= x < len(topographic_map[0]) and 0 <= y < len(topographic_map)


def get_possible_directions(pos, topographic_map):
    pos_height = int(topographic_map[pos[1]][pos[0]])
    if pos_height == 9:
        return -1
    possible_directions = []
    # Up, down, right, left
    dirs = (pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)
    for _dir in dirs:
        if within_bounds(_dir, topographic_map):
            if get_height(_dir, topographic_map) == str(pos_height + 1):
                possible_directions.append(_dir)
    return possible_directions


def calculate_trailhead_score(start_pos, topographic_map):
    score = set()
    possible_directions = get_possible_directions(start_pos, topographic_map)
    if possible_directions == -1:
        score.add(start_pos)
    else:
        for direction_pos in possible_directions:
            score.update(calculate_trailhead_score(direction_pos, topographic_map))
    return score


if __name__ == "__main__":
    topographic_map = get_map()
    trail_heads = get_trailheads(topographic_map)
    score_sum = 0
    for trail_head in trail_heads:
        score_sum += len(calculate_trailhead_score(trail_head, topographic_map))
    print("Part 1:", score_sum)
