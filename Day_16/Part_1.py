import heapq


def get_labyrinth():
    with open('input.txt', 'r') as file:
        grid = []
        end_pos = (0, 0)
        start_pos = (0, 0)
        for y, line in enumerate(file):
            grid.append(line.strip())
            if "S" in line:
                start_pos = (line.index("S"), y)
            if "E" in line:
                end_pos = (line.index("E"), y)
        return grid, end_pos, start_pos


def get_directions(labyrinth, pos):
    dirs = []
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for move in moves:
        new_x, new_y = pos[0] + move[0], pos[1] + move[1]
        if labyrinth[new_y][new_x] != "#":
            dirs.append((new_x, new_y))
    return dirs


def calculate_turns(path):
    if len(path) < 3:
        return 0

    turns = 0
    for i in range(1, len(path) - 1):
        prev_direction = (path[i][0] - path[i - 1][0], path[i][1] - path[i - 1][1])
        next_direction = (path[i + 1][0] - path[i][0], path[i + 1][1] - path[i][1])
        if prev_direction != next_direction:
            turns += 1

    return turns


def find_path_least_turns_and_shortest(labyrinth, start_pos, end_pos):
    priority_queue = [(0, 0, start_pos, [start_pos])]
    visited = {}

    while priority_queue:
        current_turns, path_length, current_pos, path = heapq.heappop(priority_queue)

        if current_pos == end_pos:
            return path

        if current_pos in visited:
            visited_turns, visited_length = visited[current_pos]
            if visited_turns < current_turns or (visited_turns == current_turns and visited_length <= path_length):
                continue
        visited[current_pos] = (current_turns, path_length)

        for direction in get_directions(labyrinth, current_pos):
            if direction not in path:
                new_path = path + [direction]
                new_turns = calculate_turns(new_path)
                new_length = len(new_path)
                heapq.heappush(priority_queue, (new_turns, new_length, direction, new_path))

    return None


if __name__ == "__main__":
    labyrinth, end_pos, start_pos = get_labyrinth()

    path_least_turns_and_shortest = find_path_least_turns_and_shortest(labyrinth, start_pos, end_pos)

    if path_least_turns_and_shortest:
        score = (calculate_turns(path_least_turns_and_shortest) + 1) * 1000 + len(path_least_turns_and_shortest) - 1
        print("Part 1:", score)
    else:
        print("No path...")
