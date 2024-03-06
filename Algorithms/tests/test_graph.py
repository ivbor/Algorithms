import pytest
import copy
import logging
import random

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


@pytest.fixture
def graphs():
    structures = [UndirectedGraph, DirectedGraph, WeightedGraph]
    return structures


@pytest.fixture
def nodes():
    nodes = [(3, []), (3, [], []), (3, [], [], [])]
    return nodes


def test_graphs_can_accept_vertex(graphs, nodes):
    graph_instance = []
    for nr, graph in enumerate(graphs):
        graph_instance.append(graph())
        graph_instance[nr].add_vertex(*nodes[nr])
        assert graph_instance[nr].all_vertices() == ['3']


@pytest.fixture
def nodes2():
    nodes2 = [(4, []), (4, [], []), (4, [], [], [])]
    return nodes2


def test_graphs_can_accept_two_unconnected_vertices(graphs, nodes, nodes2):
    graph_instance = []
    for nr, graph in enumerate(graphs):
        graph_instance.append(graph())
        graph_instance[nr].add_vertex(*nodes[nr])
        graph_instance[nr].add_vertex(*nodes2[nr])
        assert graph_instance[nr].all_vertices() == ['3', '4']


def test_find_kwarg(graphs, nodes):
    graph_instance = []
    nodes2 = \
        [{'data': 4, 'edges': []},
         {'data': 4, 'edges': [], 'directions': []},
         {'data': 4, 'edges': [], 'directions': [], 'weights': []}]
    for nr, graph in enumerate(graphs):
        graph_instance.append(graph())
        graph_instance[nr].add_vertex(*nodes[nr])
        graph_instance[nr].add_vertex(**nodes2[nr])
        assert graph_instance[nr].all_vertices() == ['3', '4']


def test_find_kwarg_with_edges(graphs, nodes):
    graph_instance = []
    nodes2 = \
        [{'data': 4, 'edges': [0]},
         {'data': 4, 'edges': [0], 'directions': [1]},
         {'data': 4, 'edges': [0], 'directions': [-1], 'weights': [5]}]
    for nr, graph in enumerate(graphs):
        graph_instance.append(graph())
        graph_instance[nr].add_vertex(*nodes[nr])
        graph_instance[nr].add_vertex(**nodes2[nr])
        assert graph_instance[nr].all_vertices() == ['3', '4']


@pytest.fixture
def uncon2(graphs, nodes, nodes2):
    graph_instance = []
    for nr, graph in enumerate(graphs):
        graph_instance.append(graph())
        graph_instance[nr].add_vertex(*nodes[nr])
        graph_instance[nr].add_vertex(*nodes2[nr])
    return graph_instance


@pytest.mark.parametrize('index_rem, all_vertices, first',
                         [(0, ['4'], '4'), (1, ['3'], '3')])
def test_can_remove_vertices_by_index(uncon2, index_rem, all_vertices, first):
    graph_instance = uncon2
    for nr in range(len(graph_instance)):
        graph_instance[nr].remove_vertex(index=index_rem)
        assert graph_instance[nr].all_vertices() == all_vertices
        assert str(graph_instance[nr].vertices[0]) == first
        assert graph_instance[nr].vertices[0].edges == []
        with pytest.raises(Exception):
            graph_instance[nr].vertices[1]
    for nr in range(len(graph_instance)):
        graph_instance[nr].remove_vertex(index=0)
        assert graph_instance[nr].all_vertices() == []
        with pytest.raises(Exception):
            graph_instance[nr].vertices[0]


@pytest.mark.parametrize('data_rem, all_vertices, first, second',
                         [(3, ['4'], '4', 4), (4, ['3'], '3', 3)])
def test_can_remove_vertices_by_data(uncon2, data_rem, all_vertices,
                                     first, second):
    graph_instance = uncon2
    for nr in range(len(graph_instance)):
        graph_instance[nr].remove_vertex(data=data_rem)
        assert graph_instance[nr].all_vertices() == all_vertices
        assert str(graph_instance[nr].vertices[0]) == first
        assert graph_instance[nr].vertices[0].edges == []
        with pytest.raises(Exception):
            graph_instance[nr].vertices[1]
    for nr in range(len(graph_instance)):
        graph_instance[nr].remove_vertex(data=second)
        assert graph_instance[nr].all_vertices() == []
        with pytest.raises(Exception):
            graph_instance[nr].vertices[0]


def test_raises_when_no_data_or_index_specified_in_remove(uncon2):
    with pytest.raises(TypeError):
        for nr in range(len(uncon2)):
            uncon2[nr].remove_vertex()


@pytest.mark.parametrize('front, back', [(0, 1), (1, 0)])
def test_add_edge_between_vertices_undir(uncon2, front, back):
    graph = uncon2[0]
    instances = [graph, copy.deepcopy(graph)]
    instances[0].add_edge(front, back)
    instances[1].add_edge(back, front)
    for instance in instances:
        assert instance.vertices[front].edges == [back]
        assert instance.vertices[back].edges == [front]


@pytest.mark.parametrize('direction, front, back', [(0, 0, 1),
                                                    (0, 1, 0),
                                                    (1, 0, 1),
                                                    (1, 1, 0),
                                                    (-1, 0, 1),
                                                    (-1, 1, 0)])
def test_add_edge_between_vertices_dir(uncon2, direction, front, back):
    instances = [uncon2[1], copy.deepcopy(uncon2[1])]
    assert instances[0].vertices[front].directions == []
    assert instances[0].vertices[back].directions == []
    assert instances[1].vertices[front].directions == []
    assert instances[1].vertices[back].directions == []
    instances[0].add_edge(front, back, direction)
    instances[1].add_edge(back, front, direction)
    assert instances[0].vertices[front].directions == [direction]
    assert instances[0].vertices[back].directions == [-direction]
    assert instances[1].vertices[front].directions == [-direction]
    assert instances[1].vertices[back].directions == [direction]


@pytest.mark.parametrize('direction, weights', [(0, [3, 4]),
                                                (0, [3]),
                                                (0, [0, 3]),
                                                (0, []),
                                                (1, [4, 3]),
                                                (1, [0, 3]),
                                                (1, [3]),
                                                (1, [])])
def test_add_edge_between_vertices_wei(uncon2, direction, weights):
    graph = uncon2[2]
    instances = [graph, copy.deepcopy(graph)]
    instances[0].add_edge(direction, int(not direction), weights=weights)
    instances[1].add_edge(int(not direction), direction, weights=weights)
    if len(weights) == 1:
        weights.append(0)
    elif len(weights) == 0:
        weights = [0, 0]
    if not direction:
        assert instances[0].vertices[0].weights == [weights[0]]
        assert instances[1].vertices[1].weights == [weights[0]]
        assert instances[0].vertices[1].weights == [weights[1]]
        assert instances[1].vertices[0].weights == [weights[1]]
    else:
        assert instances[0].vertices[0].weights == [weights[1]]
        assert instances[1].vertices[1].weights == [weights[1]]
        assert instances[0].vertices[1].weights == [weights[0]]
        assert instances[1].vertices[0].weights == [weights[0]]


def test_graphs_can_accept_two_connected_vertices(graphs, nodes):
    graph_instance = []
    nodes2 = [(4, [0]), (4, [0], [-1]), (4, [0], [1], [3])]
    for nr, graph in enumerate(graphs):
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
def con2(graphs, nodes):
    con2 = []
    nodes2 = [(4, [0]), (4, [0], [-1]), (4, [0], [1], [3])]
    for nr, graph in enumerate(graphs):
        con2.append(graph())
        con2[nr].add_vertex(*nodes[nr])
        con2[nr].add_vertex(*nodes2[nr])
        if graph == WeightedGraph:
            con2[nr].vertices[0].weights[
                    con2[nr].vertices[0].edges.index(1)] = 5
    return con2


@pytest.mark.parametrize('front, back', [(0, 1), (1, 0)])
def test_remove_edge(con2, front, back):
    for graph in con2:
        graph.remove_edge(front, back)
        if isinstance(graph, DirectedGraph):
            assert graph.vertices[0].directions == []
            assert graph.vertices[1].directions == []
        if isinstance(graph, WeightedGraph):
            assert graph.vertices[0].weights == []
            assert graph.vertices[1].weights == []
        assert graph.vertices[0].edges == []
        assert graph.vertices[1].edges == []


@pytest.mark.parametrize('params', [({'index': 0}),
                                    ({'index': 1}),
                                    ({'data': 3}),
                                    ({'data': 4})])
def test_remove_vertex(con2, params):
    for graph in con2:
        graph.remove_vertex(**params)
        assert len(graph.vertices) == 1
        last_index = [vertex.index for vertex in graph.vertices][0]
        if 'index' in params.keys():
            if params['index'] == 0:
                assert last_index == 1
                assert graph.vertices[1].edges == []
                if isinstance(graph, DirectedGraph):
                    assert graph.vertices[1].directions == []
                if isinstance(graph, WeightedGraph):
                    assert graph.vertices[1].weights == []
            else:
                assert last_index == 0
                assert graph.vertices[0].edges == []
                if isinstance(graph, DirectedGraph):
                    assert graph.vertices[0].directions == []
                if isinstance(graph, WeightedGraph):
                    assert graph.vertices[0].weights == []
        else:
            if params['data'] == 3:
                assert last_index == 1
                assert graph.vertices[1].edges == []
                if isinstance(graph, DirectedGraph):
                    assert graph.vertices[1].directions == []
                if isinstance(graph, WeightedGraph):
                    assert graph.vertices[1].weights == []
            else:
                assert last_index == 0
                assert graph.vertices[0].edges == []
                if isinstance(graph, DirectedGraph):
                    assert graph.vertices[0].directions == []
                if isinstance(graph, WeightedGraph):
                    assert graph.vertices[0].weights == []
        graph.remove_vertex(index=last_index)
        assert len(graph.vertices) == 0


def test_add_vertices_manipulate_edges_remove_vertices():
    edges = [[4, 3, 2, 1], [0, 2, 4, 3], [3, 1, 4, 0],
             [2, 4, 1, 0], [2, 1, 3, 0]]
    directions = \
        [[1, -1, 0, -1], [1, -1, 0, -1], [-1, 1, 0, 0],
         [1, -1, 1, 1], [0, 0, -1, 1]]
    weights = [[random.uniform(-100, 100) for _ in range(4)]
               for _ in range(5)]
    undir = UndirectedGraph()
    direc = DirectedGraph()
    weigh = WeightedGraph()
    graphs = [undir, direc, weigh]
    for i in range(5):
        for graph in graphs:
            graph.add_vertex(data=10*i)
            assert len(graph.all_vertices()) == i + 1
            assert graph.vertices[i].data == 10*i
    for i in range(5):
        for graph in graphs:
            graph.vertices[i].edges = copy.deepcopy(edges[i])
            if type(graph) == UndirectedGraph:
                assert graph.vertices[i].edges == edges[i]
            if type(graph) == DirectedGraph:
                graph.vertices[i].directions = copy.deepcopy(directions[i])
                assert graph.vertices[i].edges == edges[i]
                assert graph.vertices[i].directions == directions[i]
            if type(graph) == WeightedGraph:
                graph.vertices[i].directions = copy.deepcopy(directions[i])
                graph.vertices[i].weights = copy.deepcopy(weights[i])
                assert graph.vertices[i].edges == edges[i]
                assert graph.vertices[i].directions == directions[i]
                assert graph.vertices[i].weights == weights[i]
    undir.remove_edge(0, 4)
    assert len(undir.vertices[0].edges) == 3
    assert undir.vertices[0].edges == [3, 2, 1]
    assert len(undir.vertices[4].edges) == 3
    assert undir.vertices[4].edges == [2, 1, 3]
    direc.remove_edge(1, 3)
    assert len(direc.vertices[1].edges) == 3
    assert direc.vertices[1].edges == [0, 2, 4]
    assert len(direc.vertices[1].directions) == 3
    assert direc.vertices[1].directions == [1, -1, 0]
    assert len(direc.vertices[3].edges) == 3
    assert direc.vertices[3].edges == [2, 4, 0]
    assert len(direc.vertices[3].directions) == 3
    assert direc.vertices[3].directions == [1, -1, 1]
    weigh.remove_edge(2, 0)
    assert len(weigh.vertices[2].edges) == 3
    assert weigh.vertices[2].edges == [3, 1, 4]
    assert len(weigh.vertices[2].directions) == 3
    assert weigh.vertices[2].directions == [-1, 1, 0]
    assert len(weigh.vertices[2].weights) == 3
    assert len(weigh.vertices[0].edges) == 3
    assert weigh.vertices[0].edges == [4, 3, 1]
    assert len(weigh.vertices[0].directions) == 3
    assert weigh.vertices[0].directions == [1, -1, -1]
    assert len(weigh.vertices[0].weights) == 3
    undir.add_edge(0, 4)
    assert len(undir.vertices[0].edges) == 4
    assert undir.vertices[0].edges == [3, 2, 1, 4]
    assert len(undir.vertices[4].edges) == 4
    assert undir.vertices[4].edges == [2, 1, 3, 0]
    direc.add_edge(1, 3, -1)
    assert len(direc.vertices[1].edges) == 4
    assert direc.vertices[1].edges == [0, 2, 4, 3]
    assert len(direc.vertices[1].directions) == 4
    assert direc.vertices[1].directions == [1, -1, 0, -1]
    assert len(direc.vertices[3].edges) == 4
    assert direc.vertices[3].edges == [2, 4, 0, 1]
    assert len(direc.vertices[3].directions) == 4
    assert direc.vertices[3].directions == [1, -1, 1, 1]
    new_weights = \
        [random.uniform(-100, 100), random.uniform(-100, 100)]
    weigh.add_edge(2, 0, -1, new_weights)
    assert len(weigh.vertices[0].edges) == 4
    assert len(weigh.vertices[0].directions) == 4
    assert len(weigh.vertices[0].weights) == 4
    assert len(weigh.vertices[2].edges) == 4
    assert len(weigh.vertices[2].directions) == 4
    assert len(weigh.vertices[2].weights) == 4
    assert weigh.vertices[2].edges[-1] == 0
    assert weigh.vertices[2].directions[-1] == -1
    assert weigh.vertices[2].weights[-1] == new_weights[0]
    assert weigh.vertices[0].edges[-1] == 2
    assert weigh.vertices[0].directions[-1] == 1
    assert weigh.vertices[0].weights[-1] == new_weights[1]
    
    edges_changed = edges
    directions_changed = directions
    weights_changed = weights
    for i in range(5):
        # the vertex to delete
        index = random.choice([vertex.index for vertex in undir.vertices])
        # index of the vertex to delete in edges of each vertex
        indexes_in_edges = [edges_changed[i].index(index) if i != index else None for i in range(len(edges_changed))]
        assert len(indexes_in_edges) == (5 - i)
        # simulation of the vertex removal
        for nr, vertex in enumerate(undir.vertices):
            if indexes_in_edges[nr] is None:
                del edges_changed[nr]
                del directions_changed[nr]
                del weights_changed[nr]
                continue
            del edges_changed[nr][indexes_in_edges[nr]]
            del directions_changed[nr][indexes_in_edges[nr]]
            del weights_changed[nr][indexes_in_edges[nr]]
        assert len(indexes_in_edges) == (5 - i - 1)
        # now remove vertex from the graph
        assert len(undir.vertices) == (5 - i)
        for graph in [undir, direc, weigh]:
            graph.remove_vertex(index)
            assert len(graph.vertices) == (5 - i - 1)
            assert graph.edges == edges_changed
            if isinstance(graph, DirectedGraph):
                assert graph.directions == directions_changed
            if isinstance(graph, WeightedGraph):
                assert graph.weights == weights_changed