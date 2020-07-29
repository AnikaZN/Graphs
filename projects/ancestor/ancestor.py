from util import Stack, Queue

def get_neighbors(node, ancestors):
    cache = {}

    for ancestor in ancestors:
        if ancestor[0] in cache:
            cache[ancestor[0]].append(ancestor[1])
        else:
            cache[ancestor[0]] = []
            cache[ancestor[0]].append(ancestor[1])

    parents = []

    for parent in cache:
        children = cache[parent]
        for child in children:
            if child == node:
                parents.append(parent)

    if len(parents) == 0:
        return -1

    return parents

def earliest_ancestor(ancestors, starting_node):
    q = Queue()
    q.enqueue([starting_node])

    visited = set()

    paths = {}

    while q.size() > 0:
        path = q.dequeue()
        current_node = path[-1]

        if current_node not in visited:
            visited.add(current_node)

            parents = get_neighbors(current_node, ancestors)

            if parents == -1:
                return -1

            for parent in parents:
                new_path = path.copy()
                new_path.append(parent)
                grandparents = get_neighbors(parent, ancestors)

                if grandparents == -1:
                    if len(new_path) in paths:
                        paths[len(new_path)].append(new_path)
                    else:
                        paths[len(new_path)] = []
                        paths[len(new_path)].append(new_path)
                else:
                    new_path.append(grandparents[0])
                    paths[len(new_path)] = new_path

            greatest_index = max([k for k in paths])

            if type(paths[greatest_index][0]) is not int and len(paths[greatest_index][0]) > 2:
                ancestors = []
                for ancestor in paths[greatest_index][0]:
                    ancestors.append(ancestor)
                return min(ancestors)
            elif type(paths[greatest_index][0]) is int:
                return paths[greatest_index][-1]
            else:
                return paths[greatest_index][0][-1]

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 6))
