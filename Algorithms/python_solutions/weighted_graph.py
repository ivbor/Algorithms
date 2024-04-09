import heapq
import random
import logging

from Algorithms.python_solutions.graph_nodes import WeightedGraphNode
from Algorithms.python_solutions.graph import Graph


class WeightedGraph(Graph):

    def __init__(self):
        super().__init__()
        self.negative_edge_weight = False
        self.node_type = WeightedGraphNode

    def add_vertex(self, *args, **kwargs):
        super().add_vertex(*args, **kwargs)

    def add_edge(self, u: int, v: int, *args, **kwargs):
        super().add_edge(u, v, *args, **kwargs)

        # case of many weights
        weights = \
            self._find_arg([], {0: 'weights'}, *args, **kwargs)
        if len(weights) != 0:
            self.add_weight(u, v, weights[kwargs['nr']])
            return

        # case of 1 weight
        weight = \
            self._find_arg([], {0: 'weight'}, *args, **kwargs)
        if isinstance(weight, int) or isinstance(weight, float):
            self.add_weight(u, v, weight)
        elif len(weight) == 0:
            self.add_weight(u, v)

    def add_weight(self, u: int, v: int, u_to_v_weight: float = 1):

        self.vertices[u].edges[v].weight = u_to_v_weight

        if u_to_v_weight < 0:
            self.negative_edge_weight = True

    def remove_edge(self, u: int, v: int):
        super().remove_edge(u, v)

    def calculate_element(self, vertex, neighbor):
        return self.vertices[vertex].edges[neighbor].weight

    def prims_algorithm_mst(self):

        # Initializations
        try:
            start = random.choice(self.vertices).index
        except IndexError:
            return []
        visited = set([start])
        edges = \
            [(edge.weight, edge.first_node, edge.second_node)
             for edge in self.vertices[start].edges.values()]
        heapq.heapify(edges)
        mst_edges = []

        # Main loop to process all vertices
        while edges and len(visited) < len(self.vertices):
            weight, frm, to = heapq.heappop(edges)
            if to not in visited:
                visited.add(to)
                mst_edges.append((frm, to, weight))
                for edge in self.vertices[to].edges.values():
                    next_to = edge.second_node
                    next_weight = edge.weight
                    if next_to not in visited:
                        heapq.heappush(edges, (next_weight, to, next_to))

        return mst_edges

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskals_mst(self):
        result = []  # This will store the resultant MST
        i = 0  # An index variable, used for sorted edges
        e = 0  # An index variable, used for result[]

        all_edges = []
        for vertex in self.vertices:
            for _, edge in vertex.edges.items():
                first = edge.first_node
                second = edge.second_node
                weight = edge.weight
                if (weight, first, second) not in all_edges:
                    all_edges.append((weight, first, second))
        all_edges.sort(key=lambda item: item[0])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(len(self.vertices)):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < len(self.vertices) - 1:

            # Step 2: Pick the smallest edge and increment the index
            # for next iteration
            w, v, u = all_edges[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does't cause cycle,
            # include it in result and increment the index of result
            # for next edge
            if x != y:
                e = e + 1
                result.append((v, u, w))
                self.union(parent, rank, x, y)
        return result
