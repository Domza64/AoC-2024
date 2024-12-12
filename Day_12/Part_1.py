def get_garden_grid():
    with open('input.txt', 'r') as file:
        garden_grid = []
        for line in file:
            garden_grid.append(list(line.strip()))
        return garden_grid


def calculate_area(plot_pos, garden_grid, checked):
    checked.add(plot_pos)
    area = 1
    perimeter = 0
    plot = garden_grid[plot_pos[1]][plot_pos[0]]

    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for dx, dy in directions:
        nx, ny = plot_pos[0] + dx, plot_pos[1] + dy
        if 0 <= ny < len(garden_grid) and 0 <= nx < len(garden_grid[0]):
            # Neighbour withing bounds of grid
            neighbour = garden_grid[ny][nx]
            if neighbour == plot:
                if (nx, ny) not in checked:
                    result = calculate_area((nx, ny), garden_grid, checked)
                    perimeter += result[1]
                    area += result[0]
            else:
                # Neighbour is in grid but not same type so just add perimeter
                perimeter += 1
        else:
            # Out of bounds of grid, just add perimeter
            perimeter += 1

    return area, perimeter


if __name__ == "__main__":
    checked = set()
    garden_grid = get_garden_grid()
    total_price = 0
    for y, row in enumerate(garden_grid):
        for x, plot in enumerate(row):
            if (x,y) not in checked:
                result = calculate_area((x, y), garden_grid, checked)
                area = result[0]
                perimeter = result[1]
                total_price += area * perimeter

    print("Part 1:", total_price)
