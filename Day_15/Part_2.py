# Not finishe: pushing boxes up/down doesnt work if there is a diagonal box above/bellow box robot is pushing.
# Not calculating coordinates properly

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
                new_column = []
                for char in column:
                    if char == "@":
                        new_column.append("@")
                        new_column.append(".")
                        robot_pos = (column.index("@") * 2, index)
                    else:
                        for i in range(2):
                            if char == "O":
                                if i == 0:
                                    new_column.append("[")
                                else:
                                    new_column.append("]")
                            else:
                                new_column.append(char)
                grid.append(new_column)
            else:
                directions.extend(list(line.strip()))

        return grid, directions, robot_pos


def print_state(warehouse_map, robot_pos, _dir="Undefined"):
    print("Robot:", robot_pos, "Dir:", _dir)
    for line in warehouse_map:
        print("".join(line))
    print("-" * 12)


def move_right(warehouse_map, robot_pos):
    col = warehouse_map[robot_pos[1]]

    robot = col.index("@")
    for index, char in enumerate(col):
        if char == "#":
            return robot_pos
        if char == "." and index > robot:
            col.pop(index)
            col.insert(robot, ".")
            break

    warehouse_map[robot_pos[1]] = col
    return col.index("@"), robot_pos[1]


def move_left(warehouse_map, robot_pos):
    col = warehouse_map[robot_pos[1]]

    robot = col.index("@")
    for index in range(robot - 1, -1, -1):
        if col[index] == "#":
            return robot_pos
        if col[index] == ".":
            col.pop(index)
            col.insert(robot, ".")
            break

    warehouse_map[robot_pos[1]] = col
    return col.index("@"), robot_pos[1]


def move_down(warehouse_map, robot_pos):
    col = warehouse_map[robot_pos[1]]
    new_col = warehouse_map[robot_pos[1] + 1]

    robot_x = col.index("@")
    y_pos = robot_pos[1] + 1
    bellow_robot = new_col[robot_x]
    if bellow_robot == ".":
        col[robot_x] = "."
        new_col[robot_x] = "@"
        return robot_pos[0], robot_pos[1] + 1
    elif bellow_robot == "[":
        while True:
            if bellow_robot == "#":
                break
            elif bellow_robot == "." and warehouse_map[y_pos][robot_x + 1] == ".":
                warehouse_map[y_pos][robot_x] = "["
                warehouse_map[y_pos][robot_x + 1] = "]"
                warehouse_map[robot_pos[1]][robot_x] = "."
                warehouse_map[robot_pos[1] + 1][robot_x] = "@"
                warehouse_map[robot_pos[1] + 1][robot_x + 1] = "."
                return robot_pos[0], robot_pos[1] + 1
            y_pos += 1
            bellow_robot = warehouse_map[y_pos][robot_x]
    elif bellow_robot == "]":
        while True:
            if bellow_robot == "#":
                break
            elif bellow_robot == "." and warehouse_map[y_pos][robot_x - 1] == ".":
                warehouse_map[y_pos][robot_x] = "]"
                warehouse_map[y_pos][robot_x - 1] = "["
                warehouse_map[robot_pos[1]][robot_x] = "."
                warehouse_map[robot_pos[1] + 1][robot_x] = "@"
                warehouse_map[robot_pos[1] + 1][robot_x - 1] = "."
                return robot_pos[0], robot_pos[1] + 1
            y_pos += 1
            bellow_robot = warehouse_map[y_pos][robot_x]
    return robot_pos


def move_up(warehouse_map, robot_pos):
    col = warehouse_map[robot_pos[1]]
    new_col = warehouse_map[robot_pos[1] - 1]

    robot_x = col.index("@")
    y_pos = robot_pos[1] - 1
    above_robot = new_col[robot_x]

    if above_robot == ".":
        col[robot_x] = "."
        new_col[robot_x] = "@"
        return robot_pos[0], robot_pos[1] - 1
    elif above_robot == "[":
        while True:
            if above_robot == "#":
                break
            elif above_robot == "." and warehouse_map[y_pos][robot_x + 1] == ".":
                warehouse_map[y_pos][robot_x] = "["
                warehouse_map[y_pos][robot_x + 1] = "]"
                warehouse_map[robot_pos[1]][robot_x] = "."
                warehouse_map[robot_pos[1] - 1][robot_x] = "@"
                warehouse_map[robot_pos[1] - 1][robot_x + 1] = "."
                return robot_pos[0], robot_pos[1] - 1
            y_pos -= 1
            above_robot = warehouse_map[y_pos][robot_x]
    elif above_robot == "]":
        while True:
            if above_robot == "#":
                break
            elif above_robot == "." and warehouse_map[y_pos][robot_x - 1] == ".":
                warehouse_map[y_pos][robot_x] = "]"
                warehouse_map[y_pos][robot_x - 1] = "["
                warehouse_map[robot_pos[1]][robot_x] = "."
                warehouse_map[robot_pos[1] - 1][robot_x] = "@"
                warehouse_map[robot_pos[1] - 1][robot_x - 1] = "."
                return robot_pos[0], robot_pos[1] - 1
            y_pos -= 1
            above_robot = warehouse_map[y_pos][robot_x]

    return robot_pos


if __name__ == "__main__":
    warehouse_map, move_directions, robot_pos = get_data()
    # print_state(warehouse_map, robot_pos)
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

    _sum = 0
    for y, col in enumerate(warehouse_map):
        for x, char in enumerate(col):
            if char == "O":
                _sum += 100 * y + x
                # print(f"O: {x, y} = {100 * y + x}")
    print("Part 2:", _sum)
