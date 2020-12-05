with open('input.txt') as input_file:
    graph = [list(line.strip()) for line in input_file]


def traverse(graph: list, move_right: int, move_down: int) -> int:
    position = 0  # index that we're at in the line
    trees = 0
    landing_spot = None

    for line in range(0, len(graph), move_down):  # From the start of the list to the end, skipping `move_down` lines
        print(f"Line Number: {line}")
        graph[line] *= len(graph)  # Extend the line to the right per question requirements
        for element in range(position, len(graph[line][:position+move_right+1])):
            if element == landing_spot:
                if graph[line][element] == '#':
                    trees += 1
            print(element, graph[line][element])
            position += 1
        position -= 1  # Start at the space directly below on our next line
        landing_spot = position
        print('---------')
        print(f"Landing spot: {landing_spot} {graph[line][landing_spot]}")

    return trees

# Test inputs
# Trying to store all of this in memory causes a MemoryError but I'm moving on..
# a = (traverse(graph, move_right=1, move_down=1))
b = (traverse(graph, move_right=3, move_down=1))
# c = (traverse(graph, move_right=5, move_down=1))
# d = (traverse(graph, move_right=7, move_down=1))
# e = (traverse(graph, move_right=1, move_down=2))

# print(a * b * c * d * e)

print(b)