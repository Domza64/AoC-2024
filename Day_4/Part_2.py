matches = 0
with open('input.txt', 'r') as file:
    lines = []
    for line in file:
        lines.append(list(line.strip()))

    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[0]) - 1):
            letter = lines[i][j]
            if letter == "A":
                word_1 = lines[i - 1][j - 1] + lines[i + 1][j + 1]
                word_2 = lines[i + 1][j - 1] + lines[i - 1][j + 1]
                if word_1 in "SMS" and word_2 in "SMS":
                    matches += 1

print(matches)
