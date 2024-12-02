import bisect

first_list = []
second_list = []

# Read file & populate lists for further precessing
with open('input.txt', 'r') as file:
    for line in file:
        split_line = line.split("   ")
        first, last = split_line[0], split_line[1]
        bisect.insort(first_list, int(first))
        bisect.insort(second_list, int(last))

total_distance = 0
for i in range(0, len(first_list)):
    d = abs(first_list[i] - second_list[i])
    total_distance += d

print("Total distance is:", total_distance)

