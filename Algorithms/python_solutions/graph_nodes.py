import copy


class BaseGraphNode:

    def __init__(self, index, data) -> None:
        self.index = index
        self.data = data

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return str(self)


class UndirectedGraphNode(BaseGraphNode):

    def __init__(self, index, data, edges=[], capacities=[]) -> None:
        super().__init__(index, data)
        self.edges = copy.deepcopy(edges)
        self.capacities = copy.deepcopy(capacities)


class DirectedGraphNode(UndirectedGraphNode):

    def __init__(self, index, data,
                 edges=[], directions=[], capacities=[]) -> None:
        if len(edges) != len(directions):
            raise KeyError('for each edge a direction (0 or 1) ' +
                           'must be specified')
        if any(direction < 0 for direction in directions):
            raise ValueError('direction can only be 0 or 1')
        super().__init__(index, data, edges, capacities)
        self.directions = copy.deepcopy(directions)


class WeightedGraphNode(DirectedGraphNode):

    def __init__(self, index, data,
                 edges=[], directions=[], weights=[], capacities=[]) -> None:
        if len(edges) != len(weights):
            raise KeyError('for each edge a weight must be specified')
        super().__init__(index, data, edges, directions, capacities)
        self.weights = copy.deepcopy(weights)
