class BaseGraphNode:

    def __init__(self, index, data, color) -> None:
        self.index = index
        self.data = data
        self.color = color

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return str(self)


class GraphNode(BaseGraphNode):

    def __init__(self, index, data, edges=[], capacities=[], color=0) -> None:
        super().__init__(index, data, color)
        self.edges = dict()
        if len(capacities) != 0 and len(edges) == len(capacities):
            for nr, edge in enumerate(edges):
                self.edges[edge] = Edge(self.index, edge,
                                        capacity=capacities[nr])
        elif len(capacities) != 0:
            raise KeyError('for each edge a capacity must be specified')


class WeightedGraphNode(GraphNode):

    def __init__(self, index, data,
                 edges=[], weights=[], capacities=[], color=0) -> None:
        if len(edges) != len(weights):
            raise KeyError('for each edge a weight must be specified')
        super().__init__(index, data, edges, capacities, color)


class Edge():

    def __init__(self, first_node: int, second_node: int, weight=1,
                 capacity=0, flow=0, color=0, *args, **kwargs) -> None:
        self.first_node = first_node
        self.second_node = second_node
        self.weight = weight
        self.capacity = capacity
        self.flow = flow
        self.color = color
