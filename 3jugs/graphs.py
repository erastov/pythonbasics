from collections import deque


def get_path(parents, start_node, target):
    node = target
    path = []
    while node != start_node:
        path.append(node)
        node = parents[node]
    path.append(start_node)
    return path[::-1]


def recursive_dfs(graph, start_node, target):
    visited = set()
    path = []

    def dfs(node):
        nonlocal visited, graph, path
        if node == target:
            return True
        if node in visited:
            return False
        visited.add(node)
        children = graph[node]
        for child in children:
            if dfs(child):
                path.append(child)
                return True

    dfs(start_node)
    if path:
        path.append(start_node)
        return path[::-1]


def basic_dfs(graph, start_node, target):
    visited = set()
    stack = [start_node]
    parents = dict()

    while stack:
        node = stack.pop()
        if node == target:
            return get_path(parents, start_node, target)
        visited.add(node)
        children = graph[node]
        for child in children[::-1]:
            if child not in stack and child not in visited:
                parents[child] = node
                stack.append(child)


def basic_bfs(graph, start_node, target):
    visited = []
    queue = deque([start_node])
    parents = dict()

    while queue:
        node = queue.pop()
        if node == target:
            return get_path(parents, start_node, node)
        visited.append(node)
        children = graph[node]
        for child in children:
            if child not in queue and child not in visited:
                parents[child] = node
                queue.appendleft(child)


def main():
    graph = [
        [1, 2, 3],
        [0, 4, 5],
        [0, 5],
        [0],
        [1],
        [1, 2, 6],
        [5]
    ]
    start = 6
    target = 0
    print(recursive_dfs(graph, start, target))  # [3, 0, 1, 5, 6]
    print(basic_dfs(graph, start, target))  # [3, 0, 1, 5, 6]
    print(basic_bfs(graph, start, target))  # [3, 0, 1, 5, 6]


if __name__ == '__main__':
    main()
