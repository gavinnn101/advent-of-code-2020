import string


def find_shiny_gold_bag(line: str) -> dict:
    child_bags = {}
    line = line.split(' ')
    for element in range(len(line)):
        if line[element] in string.digits:
            child_bags[line[element+1] + ' ' + line[element+2]] = int(line[element])

    return child_bags


def add_bags(bag_list, parent_bag) -> int:
    return sum(parent_bag[bag_type] * add_bags(bag_list, bag_list[bag_type]) + parent_bag[bag_type] for bag_type in parent_bag)


bag_list = {}
counter = 0

with open('input.txt') as input_file:
    for line in input_file:
        line = line.strip()
        parent_bag = line.split(' ')[0] + ' ' + line.split(' ')[1]
        bag_list[parent_bag] = find_shiny_gold_bag(line)

total = 0
print(bag_list)
shiny_gold = bag_list['shiny gold']
total = add_bags(bag_list, shiny_gold)

print(f"Total: {total}")
