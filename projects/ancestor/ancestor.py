# This fails 3 tests
def earliest_ancestor(ancestors, starting_node):
    cache = {}

    for ancestor in ancestors:
        cache[ancestor[0]] = ancestor[1]

    parents = []

    for parent in cache:
        child = cache[parent]
        if child == starting_node:
            parents.append(parent)

    if len(parents) == 0:
        return -1

    for parent2 in cache:
        child = cache[parent2]
        if child in parents:
            return parent2

    return parents[0]




test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 3))
