import functools

rules = {}
updates = []
with open('input.txt', 'r') as file:
    fill_updates = False
    for line in file:
        if line == "\n":
            fill_updates = True
            continue

        if fill_updates:
            updates.append(line.strip())
        else:
            key, value = line.strip().split("|")[0], line.strip().split("|")[1]
            if key not in rules:
                rules[key] = []
            rules[key].append(value)


def is_update_valid(page_list):
    index = 0
    for page in page_list:
        index += 1
        if page in rules:
            page_rules = rules[page]
            for rule in page_rules:
                if rule in page_list[:index]:
                    return False
    return True


def compare(a, b):
    if a == b:
        return 0
    if a in rules:
        numbers = rules[a]
        if b in numbers:
            return -1
        else:
            return 1
    return 0


valid_updates = []
invalid_updates = []
for update in updates:
    if is_update_valid(update.split(",")):
        valid_updates.append(update)
    else:
        invalid_updates.append(sorted(update.split(","), key=functools.cmp_to_key(compare)))

sum = 0
for valid_update in valid_updates:
    pages = valid_update.split(",")
    sum += int(pages[len(pages) // 2])

print("Solution part 1:", sum)


sum = 0
for update in invalid_updates:
    sum += int(update[len(update) // 2])

print("Solution part 2:", sum)
