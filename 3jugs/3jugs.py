from functools import partial
from graphs import basic_bfs


class Void(object):

    def __eq__(self, x):
        return True


class ImplicitGraph(object):
    get_items = None

    def __init__(self, get_items):
        self.get_items = get_items

    def __getitem__(self, node):
        return self.get_items(node)


VOID = Void()


def get_new_state(a, b, state, jug):
    new_state = list(state)
    while new_state[a] > 0 and new_state[b] < jug[b]:
        new_state[a] -= 1
        new_state[b] += 1
    return tuple(new_state)


def get_children(state, jug):
    operators = ((0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1))
    return (get_new_state(a, b, state, jug) for a, b in operators)


def main():
    jug = (8, 3, 5)
    init = (8, 0, 0)
    target = (4, VOID, 4)

    get_children_partial = partial(get_children, jug=jug)  # https://vk.cc/8EegOW
    graph = ImplicitGraph(get_children_partial)
    solve = basic_bfs(graph, init, target)

    print(solve)


if __name__ == '__main__':
    main()
