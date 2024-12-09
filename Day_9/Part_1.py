with open('input.txt', 'r') as file:
    disk_map = file.read()

individual_blocks = []
_id = 0
free_space = False
for char in disk_map:
    if not free_space:
        for i in range(int(char)):
            individual_blocks.append(_id)
        _id += 1
        free_space = True
    else:
        for i in range(int(char)):
            individual_blocks.append(".")
        free_space = False


def replace_last_num_with_dot(_list):
    for j in range(len(_list) - 1, 0, -1):
        if _list[j] != ".":
            num = int(_list[j])
            _list.pop(j)
            return num


while "." in individual_blocks:
    first_dot = individual_blocks.index(".")
    last_num = replace_last_num_with_dot(individual_blocks)

    try:
        individual_blocks[first_dot] = last_num
    except:
        individual_blocks.append(last_num)

_sum = 0
for i in range(len(individual_blocks)):
    _sum += i * individual_blocks[i]

print("Part 1:", _sum)
