def get_garden_grid():
    with open('input.txt', 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid


def get_neighbours(x, y):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return [(x + dx, y + dy) for dx, dy in directions]


def same_region_neighbours(x, y, grid):
    neighbours = get_neighbours(x, y)
    valid_neighbours = []
    for nx, ny in neighbours:
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[x][y] == grid[nx][ny]:
            valid_neighbours.append((nx, ny))
    return valid_neighbours


def calculate_corners(x, y, region):
    corner_count = 0
    for dx in (1, -1):
        for dy in (1, -1):
            is_corner = (
                    ((x, y + dy) not in region and (x + dx, y) not in region) or
                    ((x, y + dy) in region and (x + dx, y) in region and (x + dx, y + dy) not in region)
            )
            corner_count += is_corner
    return corner_count


if __name__ == "__main__":
    grid = get_garden_grid()
    total_price = 0
    remaining_plots = {(x, y) for x in range(len(grid)) for y in range(len(grid[0]))}

    while remaining_plots:
        region = set()
        frontier = {remaining_plots.pop()}

        while frontier:
            current = frontier.pop()
            region.add(current)
            new_frontier = set(same_region_neighbours(current[0], current[1], grid)) & remaining_plots
            frontier.update(new_frontier)
            remaining_plots -= new_frontier

        total_price += len(region) * sum(calculate_corners(plot[0], plot[1], region) for plot in region)

    print("Part 2:", total_price)
