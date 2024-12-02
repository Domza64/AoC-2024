import bisect


def count_occurrences(sorted_list, target):
    left = bisect.bisect_left(sorted_list, target)
    right = bisect.bisect_right(sorted_list, target)
    return right - left


first_list = []
second_list = []

# Read file & populate lists for further precessing
with open('input.txt', 'r') as file:
    for line in file:
        split_line = line.split("   ")
        first, last = split_line[0], split_line[1]
        bisect.insort(first_list, int(first))
        bisect.insort(second_list, int(last))

similarity_score = 0
for i in range(0, len(first_list)):
    e = first_list[i]
    count = count_occurrences(second_list, e)
    e *= count
    similarity_score += e

print(similarity_score)