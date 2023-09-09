from graph import Graph
from utils import dfs, dfs_transpose


GRAPH_VERTEX_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
GRAPH_VERTEX_COUNT = 8
GRAPH_VERTEX_EDGES = [
    {'v': 'A', 'w': 'B'},  # A -> B
    {'v': 'B', 'w': 'E'},  # B -> E
    {'v': 'B', 'w': 'F'},  # B -> F
    {'v': 'B', 'w': 'C'},  # B -> C
    {'v': 'C', 'w': 'G'},  # C -> G
    {'v': 'C', 'w': 'D'},  # C -> D
    {'v': 'D', 'w': 'C'},  # D -> C
    {'v': 'D', 'w': 'H'},  # D -> H
    {'v': 'E', 'w': 'A'},  # E -> A
    {'v': 'E', 'w': 'F'},  # E -> F
    {'v': 'F', 'w': 'G'},  # F -> G
    {'v': 'G', 'w': 'F'},  # G -> F
    {'v': 'H', 'w': 'G'},  # H -> G
    {'v': 'H', 'w': 'D'},  # H -> D
]


def _init_graph(g: Graph):
    for i in range(GRAPH_VERTEX_COUNT):
        g.add_v(GRAPH_VERTEX_NAMES[i])

    for edge in GRAPH_VERTEX_EDGES:
        g.add_e(**edge)


def _init_used() -> dict[str, bool]:
    result = {}

    for vertex in GRAPH_VERTEX_NAMES:
        result[vertex] = False

    return result


if __name__ == '__main__':
    graph = Graph()
    _init_graph(graph)

    used = _init_used()
    order = []

    for v in graph.next(graph.first()):
        if not used[v]:
            dfs(v, order, used, graph)

    graph_transpose = graph.get_transpose_graph()
    used = _init_used()
    component = []

    for i in range(GRAPH_VERTEX_COUNT):
        v = order[GRAPH_VERTEX_COUNT - i - 1]

        if not used[v]:
            dfs_transpose(v, component, used, graph_transpose)

            print(', '.join(component))

            component.clear()
