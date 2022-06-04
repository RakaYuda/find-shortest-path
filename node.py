graphNode = {
    'O': {
        'A': 2,
        'B': 5,
        'C': 4,
    },
    'A': {
        'B': 2,
        'D': 7,
        'F': 12,
        'O': 2,
    },
    'B': {
        'A': 2,
        'C': 1,
        'D': 4,
        'E': 3,
        'O': 5,
    },
    'C': {
        'B': 1,
        'E': 4,
        'O': 4,
    },
    'D': {
        'A': 7,
        'B': 4,
        'E': 1,
        'T': 5,
    },
    'E': {
        'B': 3,
        'C': 4,
        'D': 1,
        'T': 7,
    },
    'F': {
        'A': 12,
        'T': 3,
    },
    'T': {
        'D': 5,
        'E': 7,
        'F': 3
    }
}

def get_list_key(graph):
    list_key = []
    for key in graph:
        list_key.append(key)
    return list_key

def get_all_path(graph, start, end, path=[]):
    path = path + [start]
    listKey = get_list_key(graph)
    if start == end:
        return [path]
        # return 'Not Move'
    elif start not in listKey or end not in listKey:
        return 'Node not in list'

    paths = []
    for node in graph[start]:
        if not node in path:
            newpaths = get_all_path(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def get_node_range(graph, list):
    listAllPath = {}
    listVal = []
    rangeNode = 0;
    for i in range(len(list)):
        if i is not len(list) - 1:
            word = list[i] + list[i+1]
            listVal.append(word)

    for key in graph:
        for value in graph[key]:
            listAllPath[key+value] = graph[key][value]

    for val in listVal:
        rangeNode += listAllPath[val]

    return rangeNode

def get_shortest_path(listPath):
    if type(listPath) != list:
        return listPath
    else:
        temp_shortest = 0
        shortest_path = []
        for i in range(len(listPath)):
            rangeNode = get_node_range(graphNode, listPath[i])
            if i == 0:
                temp_shortest = rangeNode
                shortest_path.append(listPath[i])
            else:
                if  rangeNode < temp_shortest:
                    temp_shortest = rangeNode
                    shortest_path = []
                    shortest_path.append(listPath[i])
        return shortest_path

def displayBlock(Paths):
    if type(Paths) != list or len(Paths) != 1:
        print(Paths)
    else:
        for i in range(len(Paths)):
            print(Paths[i])

path = get_all_path(graphNode,'O','T')
print('Show All Possible Path')
displayBlock(path)
print('\n==============================\n')
print('Shortest Path')
displayBlock(get_shortest_path(path))





