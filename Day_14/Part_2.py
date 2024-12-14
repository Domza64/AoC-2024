WIDTH = 101
HEIGHT = 103


def get_robots():
    with open('input.txt', 'r') as file:
        robots = []
        for line in file:
            pos, velocity = line.split(" ")
            pos = [int(num) for num in pos.split("=")[1].split(",")]
            velocity = [int(num) for num in velocity.split("=")[1].split(",")]
            robots.append([pos, velocity])
        return robots


def move_robot(robot):
    # -1 cause we start counting from 0 not 1
    height = HEIGHT - 1
    width = WIDTH - 1
    pos = robot[0]
    velocity = robot[1]

    pos_x, pos_y = pos[0], pos[1]
    velocity_x, velocity_y = velocity[0], velocity[1]

    new_x = pos_x + velocity_x
    new_y = pos_y + velocity_y

    if new_x > width:
        new_x -= width + 1
    elif new_x < 0:
        new_x = width + 1 - abs(new_x)

    if new_y > height:
        new_y -= height + 1
    elif new_y < 0:
        new_y = height + 1 - abs(new_y)

    new_pos = [new_x, new_y]
    robot[0] = new_pos


def print_map(robots, second):
    positions = [robot[0] for robot in robots]

    grid = [list("." * WIDTH) for _ in range(HEIGHT)]
    for position in positions:
        grid[position[1]][position[0]] = "R"
    for line in grid:
        if "RRRRRRR" in "".join(line):
            print(f"Time: {second}s")
            for line_2 in grid:
                print("", "".join(line_2))
            print(f"|{'-' * WIDTH}|")
            break


if __name__ == "__main__":
    seconds = 10000
    robots = get_robots()
    print_map(robots, 0)
    for second in range(seconds):
        for robot in robots:
            move_robot(robot)
        print_map(robots, second + 1)

    positions = [robot[0] for robot in robots]
    q1, q2, q3, q4 = 0, 0, 0, 0
    for position in positions:
        if position[0] > WIDTH // 2:
            if position[1] > HEIGHT // 2:
                q4 += 1
            elif position[1] < HEIGHT // 2:
                q1 += 1
        elif position[0] < WIDTH // 2:
            if position[1] > HEIGHT // 2:
                q3 += 1
            elif position[1] < HEIGHT // 2:
                q2 += 1

    print("Part 1:", q1 * q2 * q3 * q4)

