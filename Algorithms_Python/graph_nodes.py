'''
Graph Nodes and Edges
=====================

This module defines a base node class for the graph nodes to inherit from
and graph nodes themselves. Also it contains a class where the graph edge
is outlined.

Classes
-------
BaseGraphNode
    A class for graph nodes to inherit from.

Edge
    A class representing the graph edge.

GraphNode
    A class representing the usual graph node.

WeightedGraphNode
    A class representing the graph node with additional support for weights.

'''


from typing import Any


class BaseGraphNode:
    """
    Base Graph Node Class

    Represents a base graph node with basic attributes and methods.
    This class is intended to be extended by other specific types of
    graph nodes.

    Attributes
    ----------
    index : int
        The index identifier of the node.

    data : any
        Data associated with the node.

    color : int
        An integer representing the node color, useful in algorithms like
        graph coloring.

    Methods
    -------
    __init__(self, index: int, data: Any, color: int) -> None
        Initialize Base Graph Node

    __str__(self) -> str
        Return a string representation of the node's data.

    __repr__(self) -> str
        Return a string representation of the node.

    """
    def __init__(self, index: int, data: Any, color: int) -> None:
        """
        Initialize a BaseGraphNode object.

        Parameters
        ----------
        index : int
            The index identifier of the node.

        data : any
            Data associated with the node.

        color : int
            The color of the node.

        Returns
        -------
        None
        """

        self.index = index
        self.data = data
        self.color = color

    def __str__(self) -> str:
        """
        Return a string representation of the node's data.

        Returns
        -------
        str
            The string representation of the data.
        """
        return str(self.data)

    def __repr__(self) -> str:
        """
        Return a string representation of the node.

        Returns
        -------
        str
            The string representation of the node.
        """
        return str(self)


class Edge():
    """
    Edge Class

    Represents an edge in a graph with attributes to manage weights,
    capacities, and flow.

    Attributes
    ----------
    first_node : int
        The index of the first node in the edge.

    second_node : int
        The index of the second node in the edge.

    weight : float
        The weight of the edge.

    capacity : int
        The capacity of the edge, used in flow algorithms.

    flow : int
        Current flow through the edge, used in flow algorithms.

    color : int
        Color of the edge, used in certain algorithms for marking.

    Methods
    -------
    __init__(self, first_node: int, second_node: int, weight: float = 1,
    capacity: int = 0, flow: int = 0, color: int = 0) -> None
        Initialize an Edge object.
    """

    def __init__(self, first_node: int, second_node: int, weight: float = 1,
                 capacity: int = 0, flow: int = 0, color: int = 0,
                 *args, **kwargs) -> None:
        """
        Initialize an Edge object.

        Parameters
        ----------
        first_node : int
            The index of the first node in the edge.

        second_node : int
            The index of the second node in the edge.

        weight : float, optional
            The weight of the edge. Defaults to 1.

        capacity : int, optional
            The capacity of the edge. Defaults to 0.

        flow : int, optional
            The current flow through the edge. Defaults to 0.

        color : int, optional
            The color of the edge. Defaults to 0.

        Returns
        -------
        None
        """

        self.first_node = first_node
        self.second_node = second_node
        self.weight = weight
        self.capacity = capacity
        self.flow = flow
        self.color = color


class GraphNode(BaseGraphNode):
    """
    Graph Node Class

    Represents a graph node with additional functionality to manage edges
    and capacities.
    Extends BaseGraphNode with edge handling capabilities.

    Attributes
    ----------
    edges : dict
        A dictionary of edges where keys are node indices
        and values are Edge objects.

    Methods
    -------
    __init__(self, index: int, data: Any, edges: list[Edge] = [],
             capacities: list[int] = [], color: int = 0) -> None
        Initialize a GraphNode object with edges and capacities.
    """

    def __init__(self, index: int, data: Any, edges: list[Edge] = [],
                 capacities: list[int] = [], color: int = 0) -> None:
        """
        Initialize a GraphNode object with optional edges and capacities.

        Parameters
        ----------
        index : int
            The index identifier of the node.

        data : any
            Data associated with the node.

        edges : list[Edge], optional
            List of indices of connected nodes. Defaults to empty list.

        capacities : list[int], optional
            List of capacities corresponding to edges. Defaults to empty list.

        color : int, optional
            The color of the node. Defaults to 0.

        Returns
        -------
        None

        Raises
        ------
        KeyError
            If the lengths of edges and capacities do not match,
            indicating an error in input.
        """
        super().__init__(index, data, color)
        self.edges = dict()
        if len(capacities) != 0 and len(edges) == len(capacities):
            for nr, edge in enumerate(edges):
                self.edges[edge] = Edge(self.index, edge,
                                        capacity=capacities[nr])
        elif len(capacities) != 0:
            raise KeyError('for each edge a capacity must be specified')


class WeightedGraphNode(GraphNode):
    """
    Weighted Graph Node Class

    Represents a graph node that manages both weights and capacities of edges.
    Extends GraphNode to include weights along with the existing attributes.

    Methods
    -------
    __init__(self, index: int, data: Any, edges: list[Edge] = [],
             weights: list[float] = [], capacities: list[int] = [],
             color: int = 0) -> None
        Initialize a WeightedGraphNode object with weights for the edges.

    Raises
    ------
    KeyError
        If the lengths of edges and weights do not match.
    """

    def __init__(self, index: int, data: Any, edges: list[Edge] = [],
                 weights: list[float] = [], capacities: list[int] = [],
                 color: int = 0) -> None:
        """
        Initialize a WeightedGraphNode object with optional weights
        for the edges.

        Parameters
        ----------
        index : int
            The index identifier of the node.

        data : any
            Data associated with the node.

        edges : list[Edge], optional
            List of indices of connected nodes. Defaults to empty list.

        weights : list[float], optional
            List of weights corresponding to edges. Defaults to empty list.

        capacities : list[int], optional
            List of capacities corresponding to edges. Defaults to empty list.

        color : int, optional
            The color of the node. Defaults to 0.

        Returns
        -------
        None

        Raises
        ------
        KeyError
            If the lengths of edges and weights do not match,
            indicating an error in input.
        """
        if len(edges) != len(weights):
            raise KeyError('for each edge a weight must be specified')
        super().__init__(index, data, edges, capacities, color)
