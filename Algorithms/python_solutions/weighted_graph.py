from Algorithms.python_solutions.graph_nodes import WeightedGraphNode
from Algorithms.python_solutions.directed_graph import DirectedGraph


class WeightedGraph(DirectedGraph):

    def __init__(self):
        super().__init__()
        self.negative_edge_weight = False
        self.node_type = WeightedGraphNode

    def add_vertex(self, *args, **kwargs):
        super().add_vertex(*args, **kwargs)

    def add_edge(self, u: int, v: int, *args, **kwargs):
        super().add_edge(u, v, *args, **kwargs)

        weights = \
            self._find_arg([], {1: 'weights'}, *args, **kwargs)
        if len(weights) == 1:
            self.add_weight(u, v, weights[0])
        elif len(weights) == 0:
            self.add_weight(u, v)

    def add_weight(self, u: int, v: int, u_to_v_weight: float = 1):

        if v == self.vertices[u].edges[-1] and \
                len(self.vertices[u].edges) > \
                len(self.vertices[u].weights):
            self.vertices[u].weights.append(u_to_v_weight)
        else:
            self.vertices[u].weights[self.vertices[u].edges.index(v)] = \
                u_to_v_weight

        if u_to_v_weight < 0:
            self.negative_edge_weight = True

    def remove_edge(self, u: int, v: int):
        if v in self.vertices[u].edges:
            del self.vertices[u].weights[self.vertices[u].edges.index(v)]
        super().remove_edge(u, v)

    def calculate_element(self, vertex, neighbor):
        index = self.vertices[vertex].edges.index(neighbor)
        return self.vertices[vertex].directions[index] * \
            self.vertices[vertex].weights[index]
