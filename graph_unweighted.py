numOfNodes = 5
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]

from typing import List

class Graph:
    def __init__(self, numOfNodes: int, edges: List[tuple]):
        self.numOfNodes = numOfNodes
        self.data = [[] for _ in range(numOfNodes)]
        for node1, node2 in edges:
            self.data[node1].append(node2)
            self.data[node2].append(node1)

    def __repr__(self):
        return "\n".join([ "{}: {}".format(node, neighbours) for node, neighbours in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()

    def bfs(self, root):
        queue = []
        visited = []
        distance = [None] * self.numOfNodes
        parent = [None] * self.numOfNodes
        queue.append(root)
        visited.append(root)
        output = []
        distance[root] = 0
        while queue:
            currentNode = queue.pop(0)
            output.append(currentNode)
            for neighbour in self.data[currentNode]:
                if neighbour not in visited:
                    distance[neighbour] = 1 + distance[currentNode]
                    parent[neighbour] = currentNode
                    visited.append(neighbour)
                    queue.append(neighbour)
        return output, distance, parent

    def dfs(self, root):
        stack =[]
        visited = []
        stack.append(root)
        output = []
        parent = [None] * self.numOfNodes
        while stack:
            currentNode = stack.pop()
            if currentNode not in visited:
                visited.append(currentNode)
                output.append(currentNode)
                for neighbour in self.data[currentNode]:
                    parent[neighbour] = currentNode
                    if neighbour not in visited:
                        stack.append(neighbour)
        return output, parent




graph = Graph(numOfNodes, edges)
print(graph.bfs(3))
print(graph.dfs(3))
print(graph)
