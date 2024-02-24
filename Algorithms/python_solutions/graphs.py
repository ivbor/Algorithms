import logging


class UndirectedGraphNode:

    def __init__(self, data, edges=[]) -> None:
        self.data = data
        self.edges = edges

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return str(self)


class DirectedGraphNode(UndirectedGraphNode):

    def __init__(self, data, edges=[], directions=[]) -> None:
        if len(edges) != len(directions):
            raise KeyError('for each edge a direction (-1, 0 or 1) ' +
                           'must be specified')
        super().__init__(data, edges)
        self.directions = directions


class WeightedGraphNode(DirectedGraphNode):

    def __init__(self, data, edges=[], directions=[], weights=[]) -> None:
        super().__init__(data, edges, directions)
        if len(edges) != len(weights):
            raise KeyError('for each edge a weight must be specified')
        self.weights = weights


class UndirectedGraph:

    def __init__(self):
        self.vertices = []
        self.has_cycles = False
        self.node_type = UndirectedGraphNode

    def all_vertices(self):
        return [str(vertex) for vertex in self.vertices]

    def add_vertex(self, *args, **kwargs):
        new_node = self.node_type(*args, **kwargs)
        self.vertices.append(new_node)
        edges = \
            self._find_arg([], {1: 'edges'}, *args, **kwargs)
        node_nr = len(self.vertices) - 1
        for nr, edge in enumerate(edges):
            kwargs['nr'] = nr
            logging.info(kwargs)
            logging.info(args)
            if 'data' in kwargs and 'edges' in kwargs:
                self.add_edge(node_nr, edge, *args, **kwargs)
            else:
                args = args[2:]
                self.add_edge(node_nr, edge, *args, **kwargs)

    def _find_arg(self, default, arg_dict: dict[int, str], *args, **kwargs):

        pos = [i for i in arg_dict.keys()][0]
        string = [i for i in arg_dict.values()][0]

        try:
            if len(args) > pos:
                arg = args[pos]
            else:
                arg = kwargs[string]
        except KeyError:
            return default

        return arg

    def _find_index(self, **kwargs):
        if 'data' in kwargs.keys():
            index = [vertex.data for vertex in self.vertices].index(
                kwargs['data'])
        elif 'index' in kwargs.keys():
            index = kwargs['index']
        else:
            raise TypeError('no index or data specified to remove')
        return index

    def remove_vertex(self, **kwargs):
        index = self._find_index(**kwargs)
        for edge in self.vertices[index].edges:
            self.remove_edge(index, edge)
        del self.vertices[index]

    def add_edge(self, u: int, v: int, *args, **kwargs):
        if v not in self.vertices[u].edges:
            self.vertices[u].edges.append(v)
        if u not in self.vertices[v].edges:
            self.vertices[v].edges.append(u)

    def remove_edge(self, u: int, v: int):
        self.vertices[u].edges.remove(v)
        self.vertices[v].edges.remove(u)

    def bfs(self, start):

        visited = [False] * len(self.vertices)
        current_row = [start]
        visited[start] = True

        while len(current_row) != 0:
            vertex = current_row[0]
            current_row = current_row[1:]

            for neighbor in self.vertices[vertex].edges:
                if not visited[neighbor]:
                    current_row.append(neighbor)
                    visited[neighbor] = True

    def to_adjacency_matrix(self):
        matrix_size = len(self.vertices)
        adjacency_matrix = \
            [[0] * matrix_size for _ in range(matrix_size)]

        for vertex in self.vertices:
            neighbors = vertex.edges
            for neighbor in neighbors:
                adjacency_matrix[self.vertices.index(
                    vertex)][self.vertices.index(neighbor)] = \
                    self.calculate_element(vertex, neighbor)

        return adjacency_matrix

    def calculate_element(self, vertex, neighbor):
        return 1 ** (vertex + neighbor)

    def dfs(self, start_vertex, visited, end_vertex=None, sort_result=None):

        visited[start_vertex] = True

        for neighbor in self.vertices[start_vertex].edges:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, end_vertex)
            if neighbor is end_vertex:
                self.detected_cycle = True

        if sort_result is not None:
            sort_result.append(start_vertex)

    def topological_sort(self):

        visited = [False] * len(self.vertices)
        result = []

        for vertex in range(len(self.vertices)):
            if not visited[vertex]:
                self.dfs(vertex, visited, sort_result=result)

        return result[::-1]

    def cycles_detector(self, added_vertex, end_vertex):

        visited = [False] * len(self.vertices)

        self.detected_cycle = False

        for end_vertex in self.vertices[added_vertex].edges:
            if not visited[end_vertex]:
                self.dfs(added_vertex, visited, end_vertex=end_vertex)
                if self.detected_cycle:
                    return True

        return False

    def _dijkstra(self, start: int):

        # Initialize distances to all nodes as infinity
        distances = \
            [float('inf') for _ in self.vertices]
        # Set distance to start node as 0
        distances[start] = 0
        # Priority queue to store nodes to visit,
        # with their current distances
        current_distances = {start: 0}

        while current_distances:
            # Pop the node with the smallest distance from the priority queue
            current_node = \
                list(current_distances.keys())[list(
                    current_distances.values()).index(
                        min(current_distances.values()))]
            current_distance = current_distances.pop(current_node)

            # If the current distance is greater than the recorded distance,
            # skip
            if current_distance > distances[current_node]:
                continue

            # Visit each neighbor of the current node
            for neighbor in self.vertices[current_node].edges:
                distance = current_distance + \
                    self.calculate_element(current_node, neighbor)
                # If the new distance is shorter,
                # update it and add to the priority queue
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    current_distances[neighbor] = distance

        return distances

    def tarjan_dfs(self, vertex, index, stack, low_link, on_stack, scc):

        # when approach new vertex - assign it the index
        index[vertex] = self.counter
        # and the low-link value (the same one)
        # which will further show node with the lowest index
        # from which it can be accessible
        low_link[vertex] = self.counter
        self.counter += 1

        # add the current node to the current stack
        # which limits segment currently studied for connectivity
        stack.append(vertex)
        # mark the node to be in the current dfs queue
        on_stack[vertex] = True

        for neighbor in self.vertices[vertex].edges:
            # if the neighbor has not been visited yet
            if index[neighbor] == -1:
                # Recursively call DFS on the neighbor
                self.tarjan_dfs(
                    neighbor, index, stack, low_link, on_stack, scc)
                # after calling dfs to calculate low_link value
                # for neighbor update low_link value of the current node
                low_link[vertex] = min(low_link[vertex], low_link[neighbor])
            # if node is on the stack -
            # means that it has been visited earlier in the current dfs
            # but may not be updated as changes may have occurred
            # to the low_link of its neighbors on the deeper dfs iteration
            elif on_stack[neighbor]:
                low_link[vertex] = min(low_link[vertex], low_link[neighbor])

        # now that all nodes which could possibly be visited
        # on the current dfs have their indexes and we can start
        # to search for nodes in the current scc segment

        # if for vertex inside current dfs its low_link value equals to
        # its index - it is the root of the scc segment
        if low_link[vertex] == index[vertex]:
            scc_component = []
            # now - to remove vertices from current stack
            # until the root vertex is reached
            # and save them as scc segment
            while True:
                last_vertex = stack.pop()
                on_stack[last_vertex] = False
                scc_component.append(last_vertex)
                if last_vertex == vertex:
                    break
            scc.append(scc_component)

    def scc(self):

        # counter for indexes
        self.counter = 0
        # arrays of indexes and low_link values
        index = [-1] * len(self.vertices)
        low_link = [-1] * len(self.vertices)
        # array showing which of vertices are in the current dfs queue
        on_stack = [False] * len(self.vertices)
        # stack limiting segment of the graph being studied for scc
        stack = []
        # array with all found scc segments
        scc = []

        for vertex in range(len(self.vertices)):
            if index[vertex] == -1:
                self.tarjan_dfs(vertex, index, stack, low_link, on_stack, scc)

        return scc


class DirectedGraph(UndirectedGraph):

    def __init__(self):
        super().__init__()
        self.node_type = DirectedGraphNode

    def add_vertex(self, *args, **kwargs):
        super().add_vertex(*args, **kwargs)

    def add_edge(self, u: int, v: int, *args, **kwargs):
        super().add_edge(u, v)

        directions = \
            self._find_arg(0, {0: 'direction'}, *args, **kwargs)
        if isinstance(directions, list):
            self.add_direction_front(u, v, directions[kwargs['nr']])
            self.add_direction_back(u, v, directions[kwargs['nr']])
        else:
            self.add_direction_front(u, v, directions)
            self.add_direction_back(u, v, directions)

    def add_direction_front(self, u: int, v: int, direction: int = 0):

        # from u to v
        if len(self.vertices[u].directions) > v:
            self.vertices[u].directions[v] = direction
        else:
            self.vertices[u].directions.append(direction)

    def add_direction_back(self, u: int, v: int, direction: int = 0):

        # from v to u
        if len(self.vertices[v].directions) > u:
            self.vertices[v].directions[u] = -direction
        else:
            self.vertices[v].directions.append(-direction)

    def remove_edge(self, u: int, v: int):
        del self.vertices[u].directions[self.vertices[u].edges.index(v)]
        del self.vertices[v].directions[self.vertices[v].edges.index(u)]
        super().remove_edge(u, v)

    def calculate_element(self, vertex, neighbor):
        return self.vertices[vertex].directions[neighbor]


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
            self.add_weight_front(u, v, weights[0])
            self.add_weight_back(u, v)
        elif len(weights) == 0:
            self.add_weight_front(u, v)
            self.add_weight_back(u, v)
        else:
            self.add_weight_front(u, v, weights[0])
            self.add_weight_back(u, v, weights[1])

    def add_weight_front(self, u: int, v: int, u_to_v_weight: float = 0):

        if len(self.vertices[u].weights) > v:
            self.vertices[u].weights[v] = u_to_v_weight
        else:
            self.vertices[u].weights.append(u_to_v_weight)

        if u_to_v_weight < 0:
            self.negative_edge_weight = True

    def add_weight_back(self, u: int, v: int, v_to_u_weight: float = 0):

        if len(self.vertices[v].weights) > u:
            self.vertices[v].weights[u] = v_to_u_weight
        else:
            self.vertices[v].weights.append(v_to_u_weight)

        if v_to_u_weight < 0:
            self.negative_edge_weight = True

    def remove_edge(self, u: int, v: int):
        del self.vertices[u].weights[self.vertices[u].edges.index(v)]
        del self.vertices[v].weights[self.vertices[v].edges.index(u)]
        super().remove_edge(u, v)

    def calculate_element(self, vertex, neighbor):
        return self.vertices[vertex].directions[neighbor] * \
            self.vertices[vertex].weights[neighbor]

    def dijkstra(self, start):

        if self.negative_edge_weight:
            raise ValueError("Dijkstra's algorithm does not work on " +
                             "graphs where negative_edge_weight exists")

        self._dijkstra(start)
