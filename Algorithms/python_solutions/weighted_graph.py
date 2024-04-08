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
        logging.info(edges)
        heapq.heapify(edges)
        mst_edges = []

        # Main loop to process all vertices
        while edges and len(visited) < len(self.vertices):
            logging.info('vis' + str(visited))
            logging.info('turn' + str(mst_edges))
            weight, frm, to = heapq.heappop(edges)
            if to not in visited:
                visited.add(to)
                mst_edges.append((frm, to, weight))
                for edge in self.vertices[to].edges.values():
                    next_to = edge.second_node
                    next_weight = edge.weight
                    if next_to not in visited:
                        heapq.heappush(edges, (next_weight, to, next_to))
            logging.info('endcycle' + str(mst_edges))

        logging.info('endfunc' + str(mst_edges))
        return mst_edges
