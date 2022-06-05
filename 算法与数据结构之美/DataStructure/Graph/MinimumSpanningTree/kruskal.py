from functools import cmp_to_key
from Learn.DataStructure.UnionFindSet.template import UnionFindSet


def kruskal(graph: dict):
    tree, n = [], len(graph.get("nodes"))
    ufs = UnionFindSet(n + 1)
    graph.get("edges").sort(key=cmp_to_key(lambda a, b: a[2] - b[2]))
    for start, end, weight in graph.get("edges"):
        if not ufs.isSameSet(start, end):
            ufs.union(start, end)
            tree.append((start, end, weight))
    return tree


if __name__ == '__main__':
    graphData = {
        "nodes": [1, 2, 3, 4, 5],
        "edges": [(1, 2, 1),
                  (1, 3, 3),
                  (1, 4, 5),
                  (2, 3, 2),
                  (2, 4, 4),
                  (2, 5, 6)]
    }

    res = kruskal(graphData)
    print(f"Kruskal = {res}")
