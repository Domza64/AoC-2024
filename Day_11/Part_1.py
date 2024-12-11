def get_stones():
    with open('input.txt', 'r') as file:
        return [int(i) for i in file.read().split()]


if __name__ == "__main__":
    stones = get_stones()
    blinks = 25
    for i in range(blinks):
        temp_stones = []
        for stone in stones:
            if stone == 0:
                temp_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                half = int(len(str(stone)) / 2)
                temp_stones.append(int(str(stone)[:half]))
                temp_stones.append(int(str(stone)[half:]))
            else:
                temp_stones.append(str(int(stone) * 2024))
        stones = temp_stones

    print("Part 1:", len(stones))
