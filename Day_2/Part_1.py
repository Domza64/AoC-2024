def check_report(report):
    numbers = [int(n) for n in report.split(" ")]

    changes = []
    for i in range(0, len(numbers) - 1):
        c = numbers[i] - numbers[i + 1]
        changes.append(c)

    positive_changes = 0
    for n in changes:
        if n == 0 or n > 3 or n < -3:
            return False
        if n > 0:
            positive_changes += 1

    if positive_changes != 0 and positive_changes != len(changes):
        return False

    return True


safe_reports = 0

with open('input.txt', 'r') as file:
    for line in file:
        if check_report(line):
            safe_reports += 1

print("Number of safe reports:", safe_reports)