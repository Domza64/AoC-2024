from collections import defaultdict


def get_stones():
    with open('input.txt', 'r') as file:
        return [int(i) for i in file.read().split()]


def evolve_stones(start_stones, blinks):
    stone_counts = defaultdict(int)
    for stone in start_stones:
        stone_counts[stone] += 1

    for _ in range(blinks):
        new_stone_counts = defaultdict(int)

        for stone, count in stone_counts.items():
            if stone == 0:
                new_stone_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                half = len(str(stone)) // 2
                left = int(str(stone)[:half])
                right = int(str(stone)[half:])
                new_stone_counts[left] += count
                new_stone_counts[right] += count
            else:
                new_stone_counts[stone * 2024] += count

        stone_counts = new_stone_counts

    return sum(stone_counts.values())


if __name__ == "__main__":
    stones = get_stones()
    result = evolve_stones(stones, 75)
    print("Part 2:", result)

