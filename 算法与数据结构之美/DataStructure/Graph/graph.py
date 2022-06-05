from Learn.DataStructure.UnionFindSet.template import UnionFindSet


class Edge:
    def __init__(self, start=None, end=None, weight=None):
        self.start, self.end, self.weight = start, end, weight

    def __str__(self):
        return f"start = {self.start}, end = {self.end}, weight = {self.weight}"


class Graph:
    def __init__(self):
        self.ns, self.es = 0, 0
        self.nodes, self.edges = [], []

    def addNode(self, node) -> None:
        self.ns += 1
        self.nodes.append(node)

    def addEdge(self, edge: Edge) -> None:
        self.es += 1
        self.edges.append(edge)

    def getMatrix(self):
        res = [[float("inf") for _ in range(self.ns)] for _ in range(self.ns)]
        for edge in self.edges:
            res[edge.start - 1][edge.end - 1] = edge.weight
        return res

    def kruskal(self):
        tree = []
        ufs = UnionFindSet(self.ns + 1)
        self.edges.sort(key=lambda x: x.weight)
        for edge in self.edges:
            if not ufs.isSameSet(edge.start, edge.end):
                ufs.union(edge.start, edge.end)
                tree.append(edge)
        return tree


if __name__ == '__main__':
    graph = Graph()
    graphData = {
        "nodes": [1, 2, 3, 4, 5],
        "edges": [(1, 2, 1),
                  (1, 3, 3),
                  (1, 4, 5),
                  (2, 3, 2),
                  (2, 4, 4),
                  (2, 5, 6)]
    }
    for item in graphData["nodes"]:
        graph.addNode(node=item)
    for item in graphData["edges"]:
        graph.addEdge(Edge(item[0], item[1], item[2]))

    # print(graph.getMatrix())
    for item in graph.kruskal():
        print(item)
