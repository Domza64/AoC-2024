import re


def solve_equations(a1, b1, c1, a2, b2, c2):
    determinant = a1 * b2 - a2 * b1

    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    return x, y


class Machine:
    a_price = 3
    b_price = 1

    def __init__(self, a, b, prize):
        self.a = a
        self.b = b
        self.prize = prize

    def smallest_cost(self):
        ax = self.a[0]
        ay = self.a[1]
        bx = self.b[0]
        by = self.b[1]
        prize_x = self.prize[0]
        prize_y = self.prize[1]

        result = solve_equations(ax, bx, prize_x, ay, by, prize_y)
        presses_a = result[0]
        presses_b = result[1]
        if presses_a % 1 == 0 and presses_b % 1 == 0:
            return presses_a * self.a_price + presses_b * self.b_price
        return 0


def get_machines():
    machines = []
    with open('input.txt', 'r') as file:
        content = file.readlines()
        for i in range(0, len(content), 4):
            a = [int(num) for num in re.findall(r"\d+", content[i])]
            b = [int(num) for num in re.findall(r"\d+", content[i + 1])]
            prize = [int(num) for num in re.findall(r"\d+", content[i + 2])]
            prize = [prize[0] + 10000000000000, prize[1] + 10000000000000]
            machines.append(Machine(a, b, prize))
    return machines


if __name__ == "__main__":
    machines = get_machines()
    tokens_to_spend = 0
    for index, machine in enumerate(machines):
        print(f"Machine: {index + 1} of: {len(machines)}")
        tokens_to_spend += machine.smallest_cost()

    print("Part 1:", int(tokens_to_spend))
