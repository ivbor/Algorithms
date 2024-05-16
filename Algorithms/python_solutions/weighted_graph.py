"""
Weighted Graph
==============

This module implements all necessary for the Weighted Graph structure.

Classes
-------
WeightedGraph
    Advanced graph structure with ability to hold weights for all edges.

"""


import heapq
import random

from Algorithms.python_solutions.graph_nodes import WeightedGraphNode
from Algorithms.python_solutions.graph import Graph


class WeightedGraph(Graph):
    """
    Weighted Graph Class

    Represents a weighted graph structure with basic functionality, weights
    assigning and managing, as well as advanced methods to manipulate
    and analyze the graph properties.

    Space complexity of all methods where time complexity specified is O(V)
    because graph is stored as list of vertices.

    Attributes
    ----------
    negative_edge_weight: bool
        If any of edges in the graph have negative value.
        For now only Bellman-Ford algorithm depends on it and will not work
        if this value is True. Default is False.

    node_type: type
        Type of nodes which will be added to the graph.
        For WeightedGraph it is WeightedGraphNode.

    Methods
    -------
    __init__(self) -> None
        Initializes WeightedGraph.

    add_vertex(self, *args, **kwargs) -> None
        Adds vertex to the graph.

    add_edge(self, u: int, v: int, *args, **kwargs) -> None
        Adds an edge to the graph from the vertex with an index u to the one
        with an index v. Additional edge properties to be passed straight to
        the edge have to be provided in kwargs with appropriate names. Look
        Edge class in `graph_nodes.py` for more information.

    add_weight(self, u: int, v: int, u_to_v_weight: float = 1) -> None
        Adds weight to the edge.

    remove_edge(self, u: int, v: int) -> None
        Removes the edge from the vertex u to the vertex v.

    calculate_element(self, vertex: int, neighbor: int) -> float
        Calculates an element with coordinates (vertex, neighbor) of the
        adjacency matrix.

    prims_algorithm_mst(self) -> list[tuple[int, int, float]]
        Constructs a minimum spanning tree (MST) of a graph
        using Prim's algorithm.

    find(self, parent: list[int], i: int) -> int
        Finds the representative or root of the set containing `i` using
        path compression.

    union(self, parent: list[int], rank: list[int], x: int, y: int) -> None
        Performs the union of two subsets where elements `x` and `y` belong,
        using union by rank.

    kruskals_mst(self) -> list[tuple[int, int, float]]
        Constructs a minimum spanning tree (MST) of a graph using
        Kruskal's algorithm.

    bellman_ford(self, start: int) -> tuple[list[float], dict[int, list[int]]]
        Error raiser for the main bellman_ford method.
    """

    def __init__(self) -> None:
        """
        Initializes Weighted Graph.

        Parameters
        ----------
        negative_edge_weight: bool
            If any of edges in the graph have negative value.
            For now only Bellman-Ford algorithm depends on it
            and will not work if this value is True. Default is False.

        node_type: type
            Type of nodes which will be added to the graph.
            For WeightedGraph it is WeightedGraphNode.
        """
        super().__init__()
        self.negative_edge_weight = False
        self.node_type = WeightedGraphNode

    def add_vertex(self, *args, **kwargs) -> None:
        """
        Adds vertex to the graph.

        Parameters
        ----------
        kwargs['data'] or args[0]: Any
            Data to be placed into the vertex.

        kwargs['edges'] of args[1]: list[int]
            List of indexes of vertices
            with which the vertex will be connected.

        kwargs['weights'] or args[2]: list[float]
            List of weights. For each edge introduced by previous parameter
            weight has to be provided with the same index in this list as the
            appropriate vertex's index in the previous parameter.

        Returns
        -------
        None
        """
        super().add_vertex(*args, **kwargs)

    def add_edge(self, u: int, v: int, *args, **kwargs) -> None:
        """
        Adds an edge to the graph from the vertex with an index u to the one
        with an index v.

        Additional edge properties to be passed straight to
        the edge have to be provided in kwargs with appropriate names. Look
        Edge class in `graph_nodes.py` for more information.

        Parameters
        ----------
        u: int
            The index of the vertex the edge will go from.

        v: int
            The index of the vertex the edge will go to.

        kwargs['weights'] or args[0]: list[float]
            List of the weights having the weight for this edge
            under the kwargs['nr'] index. Cannot be provided
            with kwargs['weight'].
            The kwargs['nr'] is passed from super() method.

        kwargs['weight'] or args[0]: float
            Weight for the edge. Cannot be provided with kwargs['weights'].

        kwargs[...]: Any
            Additional property ... with appropriate value to be passed
            straight to the edge.

        Returns
        -------
        None
        """

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

    def add_weight(self, u: int, v: int, u_to_v_weight: float = 1) -> None:
        """
        Adds weight to the edge.

        Parameters
        ----------
        u: int
            The index of the vertex the edge
            to which weight is added goes from.

        v: int
            The index of the vertex the edge
            to which weight is added goes to.

        u_to_v_weight: float
            Weight of the edge. Default value is 1 which will be used if the
            weight is not provided.

        Returns
        -------
        None
        """
        self.vertices[u].edges[v].weight = u_to_v_weight

        if u_to_v_weight < 0:
            self.negative_edge_weight = True

    def remove_edge(self, u: int, v: int) -> None:
        """
        Removes the edge from the vertex u to the vertex v.

        Parameters
        ----------
        u: int
            The index of the vertex the edge goes from.

        v: int
            The index of the vertex the edge goes to.

        Returns
        -------
        None
        """
        super().remove_edge(u, v)

    def calculate_element(self, vertex: int, neighbor: int) -> float:
        """
        Calculates an element with coordinates (vertex, neighbor) of the
        adjacency matrix.

        Parameters
        ----------
        vertex: int
            The row of the element.

        neighbor: int
            The column of the element.

        Returns
        -------
        float
            The element of the adjacency matrix with coordinates
            (vertex, neighbor).
        """
        return self.vertices[vertex].edges[neighbor].weight

    def prims_algorithm_mst(self) -> list[tuple[int, int, float]]:
        """
        Constructs a minimum spanning tree (MST) of a graph
        using Prim's algorithm.
        Starts from a randomly chosen vertex and explores edges with
        the smallest weight, ensuring that no cycles are formed,
        to expand the MST until all vertices are included.

        Returns
        -------
        list[tuple[int, int, float]]
            Each tuple represents an edge in the MST,
            formatted as (index of the vertex starting the edge,
            index of the vertex ending the edge, weight of the edge).

        Raises
        ------
        IndexError
            If the graph is empty and no vertices are available to start
            the algorithm.
        """

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

    def find(self, parent: list[int], i: int) -> int:
        """
        Finds the representative or root of the set containing
        `i` using path compression.

        Parameters
        ----------
        parent : list[int]
            Parent array of disjoint set.
        i : int
            Element whose set representative is to be found.

        Returns
        -------
        int
            The representative of the set containing `i`.
        """
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent: list[int], rank: list[int], x: int, y: int) \
            -> None:
        """
        Performs the union of two subsets where elements `x` and `y` belong,
        using union by rank.
        Union by rank always attaches the tree with smaller height to the
        root of the tree with larger height.

        Parameters
        ----------
        parent : list[int]
            Parent array of disjoint set.

        rank : list[int]
            Rank array used for union by rank.

        x : int
            Element of the first subset.

        y : int
            Element of the second subset.

        """
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskals_mst(self) -> list[tuple[int, int, float]]:
        """
        Constructs a minimum spanning tree (MST) of a graph using
        Kruskal's algorithm.
        Sorts all edges in non-decreasing order of their weight and picks
        the smallest edge, ensuring it does not form a cycle with the MST
        formed so far. Repeats until there are V-1 edges in the MST,
        where V is the number of vertices in the graph.
        Kruskal's algorithm is suitable for graphs represented as
        an edge list and works well for sparse graphs.
        It relies heavily on a disjoint-set data structure.

        Returns
        -------
        list[tuple[int, int, float]]
            Each tuple represents an edge in the MST,
            formatted as (from_vertex, to_vertex, weight).

        """
        # This will store the resultant MST
        result = []
        # An index variable, used for sorted edges
        i = 0
        # An index variable, used for result[]
        e = 0

        all_edges = \
            [(edge['weight'], edge['first_node'], edge['second_node'])
             for edge in self.all_edges()]
        all_edges.sort(key=lambda item: item[0])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(len(self.vertices)):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < len(self.vertices) - 1:

            # Pick the smallest edge and increment the index
            # for next iteration
            w, v, u = all_edges[i][:3]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge doesn't cause cycle,
            # include it in result and increment the index of result
            # for next edge
            if x != y:
                e = e + 1
                result.append((v, u, w))
                self.union(parent, rank, x, y)
        return result

    def bellman_ford(self, start: int) \
            -> tuple[list[float], dict[int, list[int]]]:
        """
        Error raiser for the main bellman_ford method.

        Parameters
        ----------
        start: int
            Vertex to calculate distances from.

        Returns
        -------
        tuple[list[float], dict[int, list[int]]]
            Tuple with list and dict inside. In the list to each index, being
            vertex's index, corresponds the distance between it and start
            vertex. In the dict to vertices' indexes correspond the shortest
            paths between these vertices and the starting vertex,
            both included.

        Raises
        ------
        ValueError
            For graphs with negative edge weight.
        """
        if self.negative_edge_weight:
            raise ValueError('graph contains negative-weight cycles')
        return Graph.bellman_ford(self, start)
