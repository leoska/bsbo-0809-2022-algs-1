from graph import Graph


def dfs(v: str, order: list[str], used: dict[str, bool], g: Graph):
    used[v] = True

    for vertex in g.next(v):
        if not used[vertex]:
            dfs(vertex, order, used, g)

    order.append(v)


def dfs_transpose(v, component: list[str], used: dict[str, bool], g: Graph):
    used[v] = True
    component.append(v)

    for vertex in g.next(v):
        if not used[vertex]:
            dfs_transpose(vertex, component, used, g)
