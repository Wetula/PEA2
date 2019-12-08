import glob
import sys
from Graph import Graph


def to_dict(file):
    dictionary = {}
    edges = ""
    section = 0
    f = open(file, 'r')
    for line in f:
        if line.strip() == 'EDGE_WEIGHT_SECTION':
            section = 1
            pass
        elif section == 1:
            pass
        else:
            key, value = line.strip().split(':')
            dictionary[key.strip()] = value.strip()

        if section == 1:
            if dictionary['EDGE_WEIGHT_TYPE'] != 'EXPLICIT':
                sys.exit("Unsupported weight type.")
            if line.strip() != 'EOF' and line.strip() != 'EDGE_WEIGHT_SECTION':
                edges += line.replace('\n', ' ')
    dictionary['EDGES'] = edges
    return dictionary


def tsp_reader(file):
    dictionary = to_dict(file)
    size = int(dictionary['DIMENSION'])
    data = dictionary['EDGES'].split()
    graph = Graph(count=size)
    graph.make_empty_matrix()

    if dictionary['EDGE_WEIGHT_FORMAT'] == 'LOWER_DIAG_ROW':
        k = 0
        for i in range(size):
            for j in range(size):
                graph.cost_matrix[i, j] = data[k]
                graph.cost_matrix[j, i] = data[k]
                k += 1
        graph.fix_diagonal()

    elif dictionary['EDGE_WEIGHT_FORMAT'] == 'FULL_MATRIX':
        k = 0
        for i in range(size):
            for j in range(size):
                graph.cost_matrix[i, j] = data[k]
                k += 1
        graph.fix_diagonal()

    else:
        sys.exit('Unsupported weight format')

    return graph
    pass


def atsp_reader(file):
    dictionary = to_dict(file)
    size = int(dictionary['DIMENSION'])
    data = dictionary['EDGES'].split()

    graph = Graph(count=size)
    graph.make_empty_matrix()

    if dictionary['EDGE_WEIGHT_FORMAT'] != 'FULL_MATRIX':
        sys.exit('Unsupported weight format')
    else:
        k = 0
        for i in range(size):
            for j in range(size):
                graph.cost_matrix[i, j] = data[k]
                k += 1
        graph.fix_diagonal()

        print(graph.cost_matrix)
        print(size)

    return graph
    pass


def list_files():
    print("Available files:")
    print(*glob.glob('*.?tsp'), sep='\n')
