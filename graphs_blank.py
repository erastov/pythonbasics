def recursive_dfs(graph, start_node, target):
    pass


def basic_dfs(graph, start_node, target):
    pass


def basic_bfs(graph, start_node, target):
    pass


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
    start = 3
    target = 6
    print(recursive_dfs(graph, start, target))  # [3, 0, 1, 5, 6]
    print(basic_dfs(graph, start, target))  # [3, 0, 1, 5, 6]  
    print(basic_bfs(graph, start, target))  # [3, 0, 1, 5, 6]


if __name__ == '__main__':
    main()
