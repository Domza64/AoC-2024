# I'm back once again with the best algorithm... This one at least doesn't take like 2 minutes to find solution... :>

from itertools import product


def generate_operation_combinations(li, n):
    return [x for x in product(li, repeat=n)]


def can_be_true(wanted_result, number_list, operators):
    for combination in generate_operation_combinations(operators, len(number_list) - 1):
        combination_result = number_list[0]
        for i in range(len(combination)):
            for operator in combination[i]:
                if operator == "+":
                    combination_result += number_list[i + 1]
                elif operator == "|":
                    combination_result = int(str(combination_result) + str(number_list[i + 1]))
                else:
                    combination_result *= (number_list[i + 1])
        if combination_result == wanted_result:
            return True


with open('input.txt', 'r') as file:
    p1 = 0
    p2 = 0
    for line in file:
        result, numbers = line.split(":")
        result = int(result)
        numbers = [int(num) for num in numbers.strip().split(" ")]
        if can_be_true(result, numbers, ["+", "*"]):
            p1 += result
        if can_be_true(result, numbers, ["+", "*", "|"]):
            p2 += result

    print("Part 1:", p1)
    print("Part 2:", p2)