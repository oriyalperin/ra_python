from typing import Callable


def breadth_first_search(start, end, neighbor_function: Callable):
    """
    find a path between start and end. if exist one- return it. otherwise - return empty list.

    :param start: the source node (any data structure)
    :param end: the destination node (any data structure)
    :param neighbor_function: a function that finds the neighbors of a given node, and returns a list of them.
    :return: a path between the start node and the end node, if exist one. otherwise - empty list.

    Example: find a path between two 2D vectors, by vertical and horizontal steps.

        >>> start = (1,2)
        >>> end = (4,5)
        >>> def neighbor_function(node):
        ...     x, y = node[0], node[1]
        ...     return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        >>> print(breadth_first_search(start,end,neighbor_function))
        [(1, 2), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (4, 5)]


    """

    que = []
    visited = []
    prev = {}
    que.append(start)
    visited.append(start)
    while len(que) > 0:
        node = que.pop(0)
        # find the end node
        if node == end:
            # get the path
            return bfs_path(prev, [], start, end)
        else:
            neighbors = neighbor_function(node)
            for n in neighbors:
                if n not in visited:
                    que.append(n)
                    visited.append(n)
                    prev[n] = node
    return []


def bfs_path(prev: dict, path: list, start, node):
    """
    expose the path between @start and @node by lookup in @prev for each node, recursively from @node to @start.

    :param prev: dictionary of each node (as a key) and its previous node (as its value) that exposed it
    :param path: the path between the start node and node
    :param start: the source node
    :param node: the (relative) destination node
    :return: a path between the start node and the end node
    """
    path.insert(0, node)
    if node == start:
        return path
    return bfs_path(prev, path, start, prev[node])

