import pytest

from Algorithms.python_solutions.graphs import DirectedGraph, \
    DirectedGraphNode, UndirectedGraph, UndirectedGraphNode, \
    WeightedGraph, WeightedGraphNode


def test_can_create_everything():
    structures = [(UndirectedGraphNode, UndirectedGraph),
                  (DirectedGraphNode, DirectedGraph),
                  (WeightedGraphNode, WeightedGraph)]
    for node, graph in structures:
        node_instance = node(None)
        graph_instance = graph()
        assert isinstance(node_instance, node)
        assert isinstance(graph_instance, graph)
        assert graph_instance.vertices == []
        assert graph_instance.has_cycles is False
        assert node_instance.data is None


def test_undirected_graph_node_workes_well():
    structures = [UndirectedGraphNode, DirectedGraphNode, WeightedGraphNode]
    for node_type in structures:
        node = node_type(data=3)
        assert node.data == 3
        assert node.edges == []
        assert str(node) == '3'
        assert node.__repr__() == '3'
        if node_type == DirectedGraphNode:
            assert node.directions == []
            with pytest.raises(KeyError):
                node = node_type(data=3, edges=[], directions=[1])
        if node_type == WeightedGraphNode:
            assert node.weights == []
            with pytest.raises(KeyError):
                node = node_type(data=3, edges=[], directions=[1])
            with pytest.raises(KeyError):
                node = node_type(data=3, edges=[],
                                 directions=[], weights=[1, 2])


def test_graphs_can_accept_vertex():
    structures = [UndirectedGraph, DirectedGraph, WeightedGraph]
    graph_instance = []
    nodes = [(3, []), (3, [], []), (3, [], [], [])]
    for nr, graph in enumerate(structures):
        graph_instance.append(graph())
        graph_instance[nr].add_vertex(*nodes[nr])
        assert graph_instance[nr].all_vertices() == ['3']


def test_graphs_can_accept_two_unconnected_vertices():
    structures = [UndirectedGraph, DirectedGraph, WeightedGraph]
    graph_instance = []
    nodes = [(3, []), (3, [], []), (3, [], [], [])]
    nodes2 = [(4, []), (4, [], []), (4, [], [], [])]
    for nr, graph in enumerate(structures):
        graph_instance.append(graph())
        graph_instance[nr].add_vertex(*nodes[nr])
        graph_instance[nr].add_vertex(*nodes2[nr])
        assert graph_instance[nr].all_vertices() == ['3', '4']


def test_add_edge_between_vertices():
    structures = [UndirectedGraph, DirectedGraph, WeightedGraph]
    graph_instance = []
    nodes = [(3, []), (3, [], []), (3, [], [], [])]
    nodes2 = [(4, []), (4, [], []), (4, [], [], [])]
    for nr, graph in enumerate(structures):
        graph_instance.append(graph())
        graph_instance[nr].add_vertex(*nodes[nr])
        graph_instance[nr].add_vertex(*nodes2[nr])
        graph_instance[nr].add_edge(0, 1)
        assert graph_instance[nr].vertices[0].edges == [1]
        assert graph_instance[nr].vertices[1].edges == [0]


def test_graphs_can_accept_two_connected_vertices():
    structures = [UndirectedGraph, DirectedGraph, WeightedGraph]
    graph_instance = []
    nodes = [(3, []), (3, [], []), (3, [], [], [])]
    nodes2 = [(4, [0]), (4, [0], [-1]), (4, [0], [1], [3])]
    for nr, graph in enumerate(structures):
        graph_instance.append(graph())
        graph_instance[nr].add_vertex(*nodes[nr])
        graph_instance[nr].add_vertex(*nodes2[nr])
        assert graph_instance[nr].all_vertices() == ['3', '4']
        assert graph_instance[nr].vertices[1].edges == [0]
        assert graph_instance[nr].vertices[0].edges == [1]
        if graph == DirectedGraph:
            assert graph_instance[nr].vertices[1].directions == [-1]
            assert graph_instance[nr].vertices[0].directions == [1]
        if graph == WeightedGraph:
            assert graph_instance[nr].vertices[1].directions == [1]
            assert graph_instance[nr].vertices[0].directions == [-1]
            assert graph_instance[nr].vertices[1].weights == [3]
            assert graph_instance[nr].vertices[0].weights == [0]



@pytest.fixture
def undir():
    graph = UndirectedGraph()
