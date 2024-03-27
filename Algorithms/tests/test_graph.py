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
        node_instance = node(0, None)
        graph_instance = graph()
        assert isinstance(node_instance, node)
        assert isinstance(graph_instance, graph)
        assert graph_instance.vertices == {}
        assert graph_instance.has_cycles is False
        assert node_instance.data is None


def test_undirected_graph_node_workes_well():
    structures = [UndirectedGraphNode, DirectedGraphNode, WeightedGraphNode]
    for node_type in structures:
        node = node_type(index=0, data=3)
        assert node.index == 0
        assert node.data == 3
        assert node.edges == []
        assert str(node) == '3'
        assert node.__repr__() == '3'
        if node_type == DirectedGraphNode:
            assert node.directions == []
            with pytest.raises(KeyError):
                node = node_type(index=0, data=3, edges=[], directions=[1])
        if node_type == WeightedGraphNode:
            assert node.weights == []
            with pytest.raises(KeyError):
                node = node_type(index=0, data=3, edges=[], directions=[1])
            with pytest.raises(KeyError):
                node = node_type(index=0, data=3, edges=[],
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
         {'data': 4, 'edges': [0], 'directions': [1], 'weights': [5]}]
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
        assert str(graph_instance[nr].vertices[int(not index_rem)]) == first
        assert graph_instance[nr].vertices[int(not index_rem)].edges == []
        with pytest.raises(Exception):
            graph_instance[nr].vertices[index_rem]
    for nr in range(len(graph_instance)):
        graph_instance[nr].remove_vertex(index=int(not index_rem))
        assert graph_instance[nr].all_vertices() == []
        with pytest.raises(Exception):
            graph_instance[nr].vertices[index_rem]


@pytest.mark.parametrize('data_rem, all_vertices, first, second, index',
                         [(3, ['4'], '4', 4, 1), (4, ['3'], '3', 3, 0)])
def test_can_remove_vertices_by_data(uncon2, data_rem, all_vertices,
                                     first, second, index):
    graph_instance = uncon2
    for nr in range(len(graph_instance)):
        graph_instance[nr].remove_vertex(data=data_rem)
        assert graph_instance[nr].all_vertices() == all_vertices
        assert str(graph_instance[nr].vertices[index]) == first
        assert graph_instance[nr].vertices[index].edges == []
        with pytest.raises(Exception):
            graph_instance[nr].vertices[int(not index)]
    for nr in range(len(graph_instance)):
        graph_instance[nr].remove_vertex(data=second)
        assert graph_instance[nr].all_vertices() == []
        with pytest.raises(Exception):
            graph_instance[nr].vertices[index]


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
                                                    (1, 1, 0),])
def test_add_edge_between_vertices_dir(uncon2, direction, front, back):
    instances = [uncon2[1], copy.deepcopy(uncon2[1])]
    assert instances[0].vertices[front].directions == []
    assert instances[0].vertices[back].directions == []
    assert instances[1].vertices[front].directions == []
    assert instances[1].vertices[back].directions == []
    instances[0].add_edge(front, back, direction)
    instances[1].add_edge(back, front, direction)
    assert instances[0].vertices[front].directions == [direction]
    assert instances[0].vertices[back].directions == [direction]
    assert instances[1].vertices[front].directions == [direction]
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
    nodes2 = [(4, [0]), (4, [0], [1], [1]), (4, [0], [1], [3])]
    for nr, graph in enumerate(graphs):
        graph_instance.append(graph())
        graph_instance[nr].add_vertex(*nodes[nr])
        graph_instance[nr].add_vertex(*nodes2[nr])
        assert graph_instance[nr].all_vertices() == ['3', '4']
        assert graph_instance[nr].vertices[1].edges == [0]
        assert graph_instance[nr].vertices[0].edges == [1]
        if graph == DirectedGraph:
            assert graph_instance[nr].vertices[1].directions == [1]
            assert graph_instance[nr].vertices[0].directions == [1]
        if graph == WeightedGraph:
            assert graph_instance[nr].vertices[1].directions == [1]
            assert graph_instance[nr].vertices[0].directions == [1]
            assert graph_instance[nr].vertices[1].weights == [3]
            assert graph_instance[nr].vertices[0].weights == [1]


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
            if isinstance(graph, UndirectedGraph):
                assert graph.vertices[i].edges == edges[i]
            if isinstance(graph, DirectedGraph):
                graph.vertices[i].directions = copy.deepcopy(directions[i])
                assert graph.vertices[i].edges == edges[i]
                assert graph.vertices[i].directions == directions[i]
            if isinstance(graph, WeightedGraph):
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

    for graph in [undir, direc, weigh]:
        graph_edges = \
            [vertex.edges for vertex in graph.vertices]
        if isinstance(graph, DirectedGraph):
            graph_directions = \
                [vertex.directions for vertex in graph.vertices]
        if isinstance(graph, WeightedGraph):
            graph_weights = \
                [vertex.weights for vertex in graph.vertices]
        indexes_changed = [0, 1, 2, 3, 4]
        for i in range(5):
            # the vertex to delete
            index = \
                random.choice([vertex.index for vertex in graph.vertices])
            # index of the vertex to delete in edges of each vertex
            indexes_in_edges = \
                [graph_edges[j].index(index)
                    if indexes_changed[j] != index else None
                    for j in range(len(graph_edges))]

            # simulation of the vertex removal
            assert len(graph_edges) == (5 - i)
            if isinstance(graph, DirectedGraph):
                assert len(graph_directions) == (5 - i)
            if isinstance(graph, WeightedGraph):
                assert len(graph_weights) == (5 - i)
            for nr in range(len(graph.vertices)):
                assert len(graph_edges[nr]) == (5 - i - 1)
                if isinstance(graph, DirectedGraph):
                    assert len(graph_directions[nr]) == (5 - i - 1)
                if isinstance(graph, WeightedGraph):
                    assert len(graph_weights[nr]) == (5 - i - 1)
                if indexes_in_edges[nr] is None:
                    continue
                del graph_edges[nr][indexes_in_edges[nr]]
                assert len(graph_edges[nr]) == (5 - i - 2)
                if isinstance(graph, DirectedGraph):
                    del graph_directions[nr][indexes_in_edges[nr]]
                    assert len(graph_directions[nr]) == (5 - i - 2)
                if isinstance(graph, WeightedGraph):
                    del graph_weights[nr][indexes_in_edges[nr]]
                    assert len(graph_weights[nr]) == (5 - i - 2)
            del indexes_changed[indexes_changed.index(index)]
            del graph_edges[indexes_in_edges.index(None)]
            assert len(graph_edges) == (5 - i - 1)
            if isinstance(graph, DirectedGraph):
                del graph_directions[indexes_in_edges.index(None)]
                assert len(graph_directions) == (5 - i - 1)
            if isinstance(graph, WeightedGraph):
                del graph_weights[indexes_in_edges.index(None)]
                assert len(graph_weights) == (5 - i - 1)

            # now remove vertex from the graph
            assert len(graph.vertices) == (5 - i)
            graph.remove_vertex(index=index)
            assert len(graph.vertices) == (5 - i - 1)
            assert [vertex.edges for vertex in graph.vertices] == graph_edges
            if isinstance(graph, DirectedGraph):
                assert [vertex.directions for vertex in graph.vertices] == \
                    graph_directions
            if isinstance(graph, WeightedGraph):
                assert [vertex.weights for vertex in graph.vertices] == \
                    graph_weights


global weights
weights = [[random.uniform(-100, 100) for _ in range(4)] for _ in range(5)]


@pytest.fixture
def con5():
    global weights
    edges = [[4, 3, 2, 1], [0, 2, 4, 3], [3, 1, 4, 0],
             [2, 4, 1, 0], [2, 1, 3, 0]]
    directions = \
        [[1, -1, 0, -1], [1, -1, 0, -1], [-1, 1, 0, 0],
         [1, -1, 1, 1], [0, 0, 1, -1]]
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
            if isinstance(graph, UndirectedGraph):
                assert graph.vertices[i].edges == edges[i]
            if isinstance(graph, DirectedGraph):
                graph.vertices[i].directions = copy.deepcopy(directions[i])
                assert graph.vertices[i].edges == edges[i]
                assert graph.vertices[i].directions == directions[i]
            if isinstance(graph, WeightedGraph):
                graph.vertices[i].directions = copy.deepcopy(directions[i])
                graph.vertices[i].weights = copy.deepcopy(weights[i])
                assert graph.vertices[i].edges == edges[i]
                assert graph.vertices[i].directions == directions[i]
                assert graph.vertices[i].weights == weights[i]
    return graphs


@pytest.fixture
def bfs_graph():
    # 0 - 1-5
    # \\\ | |
    #    -2-6
    #  \\ | |
    #    -3-7
    #   \ | |
    #    -4-8
    graph = WeightedGraph()
    for i in range(9):
        graph.add_vertex(data=i)
    graph.vertices[0].edges = [1, 2, 3, 4]
    graph.vertices[1].edges = [0, 2, 5]
    graph.vertices[2].edges = [0, 1, 3, 6]
    graph.vertices[3].edges = [0, 2, 4, 7]
    graph.vertices[4].edges = [0, 3, 8]
    graph.vertices[5].edges = [1, 6]
    graph.vertices[6].edges = [2, 5, 7]
    graph.vertices[7].edges = [3, 6, 8]
    graph.vertices[8].edges = [4, 7]
    return graph


def test_bfs(uncon2, con2, con5, bfs_graph):
    for i in range(3):
        uncon2[i].remove_edge(0, 1)
        assert uncon2[i].vertices[0].edges == []
        assert uncon2[i].vertices[1].edges == []
        assert uncon2[i].bfs(0, 0) == [0]
        with pytest.raises(IndexError):
            uncon2[i].bfs(0, 1)
        con2[i].add_edge(0, 1)
        assert con2[i].vertices[0].edges == [1]
        assert con2[i].vertices[1].edges == [0]
        assert con2[i].bfs(0, 0) == [0]
        assert con2[i].bfs(0, 1) == [0, 1]
        for j in range(5):
            target = random.choice([0, 1, 2, 3, 4])
            while target == j:
                target = random.choice([0, 1, 2, 3, 4])
            assert con5[i].bfs(j, target) == [j, target]
        bfs_graph.vertices[0].edges = [1, 2, 3, 4]
        bfs_graph.vertices[0].directions = [1, 1, 1, 1]
        bfs_graph.vertices[1].directions = [-1, 1, 1]
        bfs_graph.vertices[2].directions = [-1, -1, 1, -1]
        bfs_graph.vertices[3].directions = [-1, -1, 1, -1]
        bfs_graph.vertices[4].directions = [-1, -1, -1]
        bfs_graph.vertices[5].directions = [-1, 1]
        bfs_graph.vertices[6].directions = [1, -1, 1]
        bfs_graph.vertices[7].directions = [1, -1, 1]
        bfs_graph.vertices[8].directions = [1, -1]
        assert bfs_graph.bfs(0, 4) == [0, 4]
        bfs_graph.vertices[0].directions = [1]
        bfs_graph.vertices[0].edges = [1]
        bfs_graph.vertices[1].edges = [2, 5]
        bfs_graph.vertices[2].edges = [1, 3, 6]
        bfs_graph.vertices[3].edges = [2, 4, 7]
        bfs_graph.vertices[4].edges = [3, 8]
        bfs_graph.vertices[1].directions = [1, 1]
        bfs_graph.vertices[2].directions = [-1, 1, -1]
        bfs_graph.vertices[3].directions = [-1, 1, -1]
        bfs_graph.vertices[4].directions = [-1, -1]
        assert bfs_graph.bfs(0, 4) == [0, 1, 2, 3, 4]


def test_adjancency_matrix(con5):
    global weights
    for i in range(3):
        if type(con5[i]) == UndirectedGraph:
            assert con5[i].to_adjacency_matrix() == [[0, 1, 1, 1, 1],
                                                     [1, 0, 1, 1, 1],
                                                     [1, 1, 0, 1, 1],
                                                     [1, 1, 1, 0, 1],
                                                     [1, 1, 1, 1, 0]]
        if type(con5[i]) == DirectedGraph:
            assert con5[i].to_adjacency_matrix() == [[0, -1, 0, -1, 1],
                                                     [1, 0, -1, -1, 0],
                                                     [0, 1, 0, -1, 0],
                                                     [1, 1, 1, 0, -1],
                                                     [-1, 0, 0, 1, 0]]
        if type(con5[i]) == WeightedGraph:
            adj_mtx = con5[i].to_adjacency_matrix()
            for row_nr in range(len(adj_mtx)):
                for col_nr in range(len(con5[i].vertices)):
                    if row_nr != col_nr:
                        index = \
                            con5[i].vertices[row_nr].edges.index(col_nr)
                        assert abs(adj_mtx[row_nr][col_nr] -
                                   con5[i].vertices[row_nr]
                                   .directions[index] *
                                   con5[i].vertices[row_nr]
                                   .weights[index]) <= 10**-6
                    else:
                        assert adj_mtx[row_nr][col_nr] == 0


def test_cycles_detector(uncon2, con5, bfs_graph):

    for i in range(3):
        assert uncon2[i].is_cyclic() is False
        assert con5[i].is_cyclic() is True

    bfs_graph.vertices[0].edges = [1]
    bfs_graph.vertices[0].directions = [1]

    bfs_graph.vertices[1].directions = [-1, -1, 1]

    bfs_graph.vertices[2].edges = [3]
    bfs_graph.vertices[2].directions = [-1]

    bfs_graph.vertices[3].edges = [2, 4]
    bfs_graph.vertices[3].directions = [1, -1]

    bfs_graph.vertices[4].edges = [3, 8]
    bfs_graph.vertices[4].directions = [1, -1]

    bfs_graph.vertices[5].directions = [-1, 1]

    bfs_graph.vertices[6].edges = [5, 7]
    bfs_graph.vertices[6].directions = [-1, 1]

    bfs_graph.vertices[7].edges = [6, 8]
    bfs_graph.vertices[7].directions = [-1, 1]

    bfs_graph.vertices[8].directions = [1, -1]
    assert bfs_graph.is_cyclic() is False


def test_topo_sort(bfs_graph):

    # error for cycle
    # 0 > 1>5
    #     ^ |
    #     2 6
    #     ^ |
    #     3 7
    #     ^ |
    #     4<8

    bfs_graph.vertices[0].edges = [1]
    bfs_graph.vertices[0].directions = [1]

    bfs_graph.vertices[1].directions = [-1, -1, 1]

    bfs_graph.vertices[2].edges = [1, 3]
    bfs_graph.vertices[2].directions = [1, -1]

    bfs_graph.vertices[3].edges = [2, 4]
    bfs_graph.vertices[3].directions = [1, -1]

    bfs_graph.vertices[4].edges = [3, 8]
    bfs_graph.vertices[4].directions = [1, -1]

    bfs_graph.vertices[5].directions = [-1, 1]

    bfs_graph.vertices[6].edges = [5, 7]
    bfs_graph.vertices[6].directions = [-1, 1]

    bfs_graph.vertices[7].edges = [6, 8]
    bfs_graph.vertices[7].directions = [-1, 1]

    bfs_graph.vertices[8].directions = [1, -1]
    with pytest.raises(RecursionError):
        bfs_graph.topological_sort()

    bfs_graph.vertices[2].edges = [3]
    bfs_graph.vertices[2].directions = [-1]
    assert bfs_graph.topological_sort() == [0, 1, 5, 6, 7, 8, 4, 3, 2]


def test_single_node():
    graph = DirectedGraph()
    graph.add_vertex(data=0)
    assert graph.scc() == [[0]]
    assert graph.kosaraju_scc() == [[0]]


def test_two_nodes_no_edge():
    graph = DirectedGraph()
    graph.add_vertex(data=0)
    graph.add_vertex(data=1)
    assert graph.scc() == [[0], [1]]
    assert sorted([sorted(scc) for scc in graph.kosaraju_scc()]) == [[0], [1]]


def test_simple_cycle():
    graph = DirectedGraph()
    graph.add_vertex(data=0)
    graph.add_vertex(data=1)
    graph.add_vertex(data=2)
    graph.add_edge(0, 1, 1)
    graph.add_edge(1, 2, 1)
    graph.add_edge(2, 0, 1)
    assert sorted([sorted(scc) for scc in graph.scc()]) == [[0, 1, 2]]
    assert sorted([sorted(scc) for scc in graph.kosaraju_scc()]) == [[0, 1, 2]]


def test_multiple_scc():
    graph = DirectedGraph()
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_edge(0, 1, 1)
    graph.add_edge(1, 2, 1)
    graph.add_edge(2, 0, 1)
    graph.add_edge(3, 2, 1)  # This creates two SCCs: {0,1,2} and {3}
    assert sorted([sorted(scc) for scc in graph.scc()],
                  key=lambda scc: scc[0]) == [[0, 1, 2], [3]]
    assert sorted([sorted(scc) for scc in graph.kosaraju_scc()],
                  key=lambda scc: scc[0]) == [[0, 1, 2], [3]]


def test_complex_graph():
    graph = DirectedGraph()
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_edge(0, 1, 1)
    graph.add_edge(1, 2, 1)
    graph.add_edge(2, 0, 1)
    graph.add_edge(2, 3, 1)
    graph.add_edge(3, 4, 1)
    graph.add_edge(4, 5, 1)
    graph.add_edge(5, 3, 1)
    # This creates two SCCs: {0,1,2} and {3,4},
    # assuming no connections between these groups
    assert sorted([sorted(scc) for scc in graph.scc()],
                  key=lambda scc: scc[0]) == [[0, 1, 2], [3, 4, 5]]
    assert sorted([sorted(scc) for scc in graph.kosaraju_scc()],
                  key=lambda scc: scc[0]) == [[0, 1, 2], [3, 4, 5]]


def test_edge_cases():
    graph = DirectedGraph()
    # Test an edge case, such as a graph with no vertices
    assert graph.scc() == []
    assert graph.kosaraju_scc() == []


def test_dijkstra_undir():
    graph = UndirectedGraph()
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 3)
    assert graph._dijkstra(0) == [0, 1, 1, 2, 3, 3]


def test_bellman_ford():
    pass