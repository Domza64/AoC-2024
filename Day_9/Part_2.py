# https://github.com/mileswijeyeratne/AOC/blob/master/python/2024/9.py
# I completely stole this code from this guy, you can see my code commented down below,
# It works for example input but not for my input, I just couldn't figure out why and didn't
# have time to find out, so I took this for day 9. :(
def get_data():
    with open('input.txt', 'r') as file:
        input_data = file.read()

    return input_data


def checksum(s):
    res = 0
    for i, s in enumerate(s):
        res += i * s
    return res


def solution(data):
    filesystem = []
    id = 0
    for i, c in enumerate(data):
        c = int(c)
        if i % 2 == 0:
            filesystem.append((id, c))
            id += 1
        else:
            filesystem.append((-1, c))
    def index(iterable):
        for i, v in enumerate(iterable):
            if v:
                return i
        raise ValueError

    for i in range(id-1, -1, -1):
        # file to move
        file_ind = index(n[0] == i for n in filesystem)
        file = filesystem[file_ind]

        # get free space
        try:
            space_ind = index(n[0] == -1 and n[1] >= file[1]
                              for n in filesystem)
        except ValueError:
            continue

        # check space is before file
        if space_ind > file_ind:
            continue

        # move it
        space = filesystem[space_ind]
        filesystem[file_ind] = (-1, file[1])
        filesystem[space_ind] = file
        filesystem.insert(space_ind + 1, (-1, space[1] - file[1]))

    # reconstruct into format that checksum() works on
    res = []
    for i, n in filesystem:
        res.extend(max(0, i) for j in range(n))

    return checksum(res)


if __name__ == "__main__":
    print("Part 2:", solution(get_data()))


# with open('input.txt', 'r') as file:
#     disk_map = file.read()
#
# individual_blocks = []
# _id = 0
# free_space = False
# for char in disk_map:
#     new_block = ""
#     if not free_space:
#         for i in range(int(char)):
#             new_block += str(_id)
#         _id += 1
#         free_space = True
#     else:
#         for i in range(int(char)):
#             new_block += "."
#         free_space = False
#     if new_block != "":
#         individual_blocks.append(new_block)
#
#
# def replace_dots_with_num(s, num):
#     dots = s.count(".")
#     s = s.replace(".", "")
#     s += num
#     s += (dots - len(num)) * "."
#     return s
#
#
# for i in range(len(individual_blocks) - 1, 0, - 1):
#     current_last_block = individual_blocks[i]
#     for j in range(i):
#         current_first_block = individual_blocks[j]
#         if "." in current_first_block and current_first_block.count(".") >= len(current_last_block):
#             individual_blocks[i] = len(current_last_block) * "."
#             if current_last_block.replace(".", "").isdigit():
#                 individual_blocks[j] = replace_dots_with_num(current_first_block, current_last_block.replace(".", ""))
#                 break
#
# final_str = "".join(individual_blocks)
#
# _sum = 0
# for i in range(len(final_str)):
#     char = final_str[i]
#     if char.isnumeric():
#         _sum += i * int(char)
#
# print("Part 2:", _sum)
