import re


def find_in_line(line):
    # Must be a way to find overlying results with regex
    return len(re.findall("XMAS", line)) + len(re.findall("SAMX", line))


matches = 0
with open('input.txt', 'r') as file:
    lines = []
    for line in file:
        # Search all horizontal lines
        matches += find_in_line(line.strip())
        lines.append(list(line.strip()))

    # Search all vertical lines
    temp_line = ""
    for i in range(len(lines[0])):
        for line in lines:
            temp_line += line[i]
        matches += find_in_line(temp_line)
        temp_line = ""

    # Solution for diagonals from: https://github.com/nitekat1124/advent-of-code-2024/blob/main/solutions/day04.py
    # from top-left to bottom-right
    main_diagonals = {}
    # from top-right to bottom-left
    anti_diagonals = {}

    for r in range(len(lines)):
        for c in range(len(lines[0])):
            key_main = r - c
            if key_main not in main_diagonals:
                main_diagonals[key_main] = []
            main_diagonals[key_main].append(lines[r][c])

            key_anti = r + c
            if key_anti not in anti_diagonals:
                anti_diagonals[key_anti] = []
            anti_diagonals[key_anti].append(lines[r][c])

    for key in anti_diagonals:
        matches += find_in_line("".join((anti_diagonals[key])))

    for key in main_diagonals:
        matches += find_in_line("".join((main_diagonals[key])))

print(matches)
