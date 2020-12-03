graph = []
with open('input.txt') as input_file:
    for line in input_file:
        graph.append(line.strip())


def traverse(graph: list, move_right: int, move_down: int) -> int:
    position = 0  # index that we're at in the line
    trees = 0
    landing_spot = None

    for line in graph:
        line *= len(graph)  # Repeat the graph per question requirements
        for element in range(position, len(line[:position+move_right+1])):
            if element == landing_spot:
                if line[element] == '#':
                    trees += 1
                    print(f"Hit a tree at {element}")
            print(element, line[element])
            position += 1
        position -= move_down
        landing_spot = position
        print('---------')

    return trees


# a = (traverse(graph, move_right=1, move_down=1))
# b = (traverse(graph, move_right=3, move_down=1))
# c = (traverse(graph, move_right=5, move_down=1))
# d = (traverse(graph, move_right=7, move_down=1))
e = (traverse(graph, move_right=1, move_down=2))

# print(a * b * c * d * e)