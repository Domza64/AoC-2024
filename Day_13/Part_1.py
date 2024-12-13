import re


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

        max_b_presses_x = prize_x // bx
        max_b_presses_y = prize_y // by
        max_a_presses_x = prize_x // ax
        max_a_presses_y = prize_y // ay

        max_b_presses = min(max_b_presses_x, max_b_presses_y)
        max_a_presses = min(max_a_presses_x, max_a_presses_y)

        min_cost = float('inf')

        for b_presses in range(max_b_presses + 1):
            for a_presses in range(max_a_presses + 1):
                total_x = a_presses * ax + b_presses * bx
                total_y = a_presses * ay + b_presses * by

                if total_x == prize_x and total_y == prize_y:
                    cost = self.a_price * a_presses + self.b_price * b_presses
                    min_cost = min(min_cost, cost)

        return min_cost if min_cost != float('inf') else 0


def get_machines():
    machines = []
    with open('input.txt', 'r') as file:
        content = file.readlines()
        for i in range(0, len(content), 4):
            a = [int(num) for num in re.findall(r"\d+", content[i])]
            b = [int(num) for num in re.findall(r"\d+", content[i + 1])]
            prize = [int(num) for num in re.findall(r"\d+", content[i + 2])]
            machines.append(Machine(a, b, prize))
    return machines


if __name__ == "__main__":
    machines = get_machines()
    tokens_to_spend = 0
    for index, machine in enumerate(machines):
        print(f"Machine: {index + 1} of: {len(machines)}")
        tokens_to_spend += machine.smallest_cost()

    print("Part 1:", tokens_to_spend)
