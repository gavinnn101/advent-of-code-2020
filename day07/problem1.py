def find_shiny_gold_bag(line: str, bag_list: list) -> str:
    target_bag = 'shiny gold'
    parent_bag = line.split(' ')[0] + ' ' + line.split(' ')[1]

    if target_bag in line and parent_bag != target_bag:
        return parent_bag

    for bag in bag_list:
        if bag in line:
            return parent_bag


bag_list = []
counter = 0

with open('input.txt') as input_file:
    for line in input_file:
        line = line.strip()
        parent_bag = find_shiny_gold_bag(line, bag_list)
        if parent_bag is not None:
            bag_list.append(parent_bag)
    print(f"End of first loop: {bag_list}")
    while counter < len(bag_list):  # Loop over until we stop finding new matches
        input_file.seek(0)  # Start from the top of the file again
        for line in input_file:
            line = line.strip()
            parent_bag = find_shiny_gold_bag(line, bag_list)
            if parent_bag is not None and parent_bag not in bag_list:
                bag_list.append(parent_bag)
                print(f"Bag List: {bag_list}")
        counter += 1


print(f"Total Bags: {len(bag_list)}")
