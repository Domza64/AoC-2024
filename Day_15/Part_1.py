def get_data():
    with open('input.txt', 'r') as file:
        grid = []
        directions = []
        robot_pos = (0, 0)
        reading_grid = True
        for index, line in enumerate(file):
            if line == "\n":
                reading_grid = False
                continue
            if reading_grid:
                column = list(line.strip())
                if "@" in column:
                    robot_pos = (column.index("@"), index)
                grid.append(column)
            else:
                directions.extend(list(line.strip()))
        return grid, directions, robot_pos


def print_state(warehouse_map, robot_pos, _dir="Undefined"):
    print("Robot:", robot_pos, "Dir:", _dir)
    for line in warehouse_map:
        print("".join(line))


def move_right(warehouse_map, robot_pos):
    hit = warehouse_map[robot_pos[1]][robot_pos[0] + 1]
    if hit == ".":
        warehouse_map[robot_pos[1]][robot_pos[0] + 1] = "@"
        warehouse_map[robot_pos[1]][robot_pos[0]] = "."
        return robot_pos[0] + 1, robot_pos[1]
    elif hit == "O":
        new_hit_pos = (robot_pos[0] + 1, robot_pos[1])
        i = 0
        while hit == "O":
            i += 1
            hit = warehouse_map[new_hit_pos[1]][new_hit_pos[0] + i]

        if hit != "#":
            # First next "." becomes new O
            warehouse_map[new_hit_pos[1]][new_hit_pos[0] + i] = "O"
            # Old robot pos = "."
            warehouse_map[robot_pos[1]][robot_pos[0]] = "."
            # Set and return new robot pos
            warehouse_map[robot_pos[1]][robot_pos[0] + 1] = "@"
            return robot_pos[0] + 1, robot_pos[1]
    return robot_pos


def move_left(warehouse_map, robot_pos):
    hit = warehouse_map[robot_pos[1]][robot_pos[0] - 1]
    if hit == ".":
        warehouse_map[robot_pos[1]][robot_pos[0] - 1] = "@"
        warehouse_map[robot_pos[1]][robot_pos[0]] = "."
        return robot_pos[0] - 1, robot_pos[1]
    elif hit == "O":
        new_hit_pos = (robot_pos[0] - 1, robot_pos[1])
        i = 0
        while hit == "O":
            i += 1
            hit = warehouse_map[new_hit_pos[1]][new_hit_pos[0] - i]

        if hit != "#":
            warehouse_map[new_hit_pos[1]][new_hit_pos[0] - i] = "O"
            warehouse_map[robot_pos[1]][robot_pos[0]] = "."
            warehouse_map[robot_pos[1]][robot_pos[0] - 1] = "@"
            return robot_pos[0] - 1, robot_pos[1]
    return robot_pos


def move_up(warehouse_map, robot_pos):
    hit = warehouse_map[robot_pos[1] - 1][robot_pos[0]]
    if hit == ".":
        warehouse_map[robot_pos[1] - 1][robot_pos[0]] = "@"
        warehouse_map[robot_pos[1]][robot_pos[0]] = "."
        return robot_pos[0], robot_pos[1] - 1
    elif hit == "O":
        new_hit_pos = (robot_pos[0], robot_pos[1] - 1)
        i = 0
        while hit == "O":
            i += 1
            hit = warehouse_map[new_hit_pos[1] - i][new_hit_pos[0]]

        if hit != "#":
            warehouse_map[new_hit_pos[1] - i][new_hit_pos[0]] = "O"
            warehouse_map[robot_pos[1]][robot_pos[0]] = "."
            warehouse_map[robot_pos[1] - 1][robot_pos[0]] = "@"
            return robot_pos[0], robot_pos[1] - 1
    return robot_pos


def move_down(warehouse_map, robot_pos):
    hit = warehouse_map[robot_pos[1] + 1][robot_pos[0]]
    if hit == ".":
        warehouse_map[robot_pos[1] + 1][robot_pos[0]] = "@"
        warehouse_map[robot_pos[1]][robot_pos[0]] = "."
        return robot_pos[0], robot_pos[1] + 1
    elif hit == "O":
        new_hit_pos = (robot_pos[0], robot_pos[1] + 1)
        i = 0
        while hit == "O":
            i += 1
            hit = warehouse_map[new_hit_pos[1] + i][new_hit_pos[0]]

        if hit != "#":
            warehouse_map[new_hit_pos[1] + i][new_hit_pos[0]] = "O"
            warehouse_map[robot_pos[1]][robot_pos[0]] = "."
            warehouse_map[robot_pos[1] + 1][robot_pos[0]] = "@"
            return robot_pos[0], robot_pos[1] + 1
    return robot_pos


if __name__ == "__main__":
    warehouse_map, move_directions, robot_pos = get_data()
    # print_state(warehouse_map, robot_pos)
    # print("-" * 12)
    for _dir in move_directions:
        if _dir == ">":
            robot_pos = move_right(warehouse_map, robot_pos)
        if _dir == "<":
            robot_pos = move_left(warehouse_map, robot_pos)
        if _dir == "^":
            robot_pos = move_up(warehouse_map, robot_pos)
        if _dir == "v":
            robot_pos = move_down(warehouse_map, robot_pos)
        # print_state(warehouse_map, robot_pos, _dir)
        # print("-" * 12)

    _sum = 0
    for y, col in enumerate(warehouse_map):
        for x, char in enumerate(col):
            if char == "O":
                _sum += 100 * y + x
                # print(f"O: {x, y} = {100 * y + x}")
    print("Part 1:", _sum)
