import re

with open('input.txt', 'r') as file:
    result = 0
    input = file.read()
    instructions = re.findall("mul\\([0-9]+,[0-9]+\\)", input)
    for instruction in instructions:
        str_numbers = re.findall("[0-9]+", instruction)
        multiplied = int(str_numbers[0]) * int(str_numbers[1])
        result += multiplied
    print(result)