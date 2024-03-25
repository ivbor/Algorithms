import logging
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

    def __init__(self, index, data, edges=[]) -> None:
        super().__init__(index, data)
        self.edges = copy.deepcopy(edges)


class DirectedGraphNode(UndirectedGraphNode):

    def __init__(self, index, data, edges=[], directions=[]) -> None:
        if len(edges) != len(directions):
            raise KeyError('for each edge a direction (-1, 0 or 1) ' +
                           'must be specified')
        super().__init__(index, data, edges)
        self.directions = copy.deepcopy(directions)


class WeightedGraphNode(DirectedGraphNode):

    def __init__(self, index, data,
                 edges=[], directions=[], weights=[]) -> None:
        if len(edges) != len(weights):
            raise KeyError('for each edge a weight must be specified')
        super().__init__(index, data, edges, directions)
        self.weights = weights


class VerticesList(list):
    def __getitem__(self, index):
        return list.__getitem__(self, self.find_index(index))

    def find_index(self, index):
        return [vertex.index for vertex in self].index(index)

    def __delitem__(self, index):
        super().__delitem__(self.find_index(index))


class UndirectedGraph:

    def __init__(self):
        self.vertices = VerticesList()
        self.has_cycles = False
        self.node_type = UndirectedGraphNode

    def all_vertices(self):
        return [str(vertex) for vertex in self.vertices]

    def add_vertex(self, *args, **kwargs):
        if len(self.vertices) == 0:
            index = len(self.vertices)
        else:
            present_indexes = [vertex.index for vertex in self.vertices]
            missing_vals = set(present_indexes).difference(
                            set([i for i in range(max(present_indexes) + 1)]))
            if len(missing_vals) != 0:
                index = min(missing_vals)
            else:
                index = max(present_indexes) + 1
        new_node = self.node_type(index, *args, **kwargs)
        self.vertices.append(new_node)
        edges = \
            self._find_arg([], {1: 'edges'}, *args, **kwargs)
        for nr, edge in enumerate(edges):
            kwargs['nr'] = nr
            if 'data' in kwargs and 'edges' in kwargs:
                self.add_edge(index, edge, *args, **kwargs)
            else:
                args = args[2:]
                self.add_edge(index, edge, *args, **kwargs)

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
            index = [vertex.index for vertex in self.vertices
                     if vertex.data == kwargs['data']][0]
        elif 'index' in kwargs.keys():
            index = kwargs['index']
        else:
            raise TypeError('no index or data specified to remove')
        return index

    def remove_vertex(self, **kwargs):
        index = self._find_index(**kwargs)
        while len(self.vertices[index].edges) != 0:
            self.remove_edge(index, self.vertices[index].edges[0])
        del self.vertices[index]

    def add_edge(self, u: int, v: int, *args, **kwargs):
        if v not in self.vertices[u].edges:
            self.vertices[u].edges.append(v)
        if u not in self.vertices[v].edges:
            self.vertices[v].edges.append(u)

    def remove_edge(self, u: int, v: int):
        if v in self.vertices[u].edges:
            self.vertices[u].edges.remove(v)
        if u in self.vertices[v].edges:
            self.vertices[v].edges.remove(u)

    def bfs(self, start):

        to_return = []
        visited = [False] * (
            max([vertex.index for vertex in self.vertices]) + 1)
        current_row = [start]
        visited[start] = True

        while len(current_row) != 0:
            vertex = current_row[0]
            to_return.append(self.vertices[vertex].data)
            current_row = current_row[1:]

            for neighbor in self.vertices[vertex].edges:
                if not visited[neighbor]:
                    current_row.append(neighbor)
                    visited[neighbor] = True
        return to_return

    def to_adjacency_matrix(self):

        matrix_size = len(self.vertices)
        adjacency_matrix = \
            [[0] * matrix_size for _ in range(matrix_size)]

        for vertex in self.vertices:
            neighbors = vertex.edges
            for neighbor in neighbors:
                adjacency_matrix[vertex.index][neighbor] = \
                    self.calculate_element(vertex.index, neighbor)

        return adjacency_matrix

    def calculate_element(self, vertex, neighbor):
        return 1 ** (vertex + neighbor)

    def dfs(self, start_vertex, visited=None, to_return=None):

        if to_return is None:
            to_return = []
        to_return.append(self.vertices[start_vertex].data)

        if visited is None:
            visited = [False] * len(self.vertices)
        visited[start_vertex] = True

        for neighbor in self.vertices[start_vertex].edges:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, to_return=to_return)

        return to_return

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

    def is_cyclic_util(self, vertex, visited, rec_stack):

        # Mark the current node as visited
        visited[vertex] = True
        rec_stack[vertex] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.vertices[vertex].edges:

            if hasattr(self.vertices[vertex], 'directions'):
                # Check if the edge direction is forward;
                # if not, skip this iteration
                direction = self.vertices[vertex]\
                    .directions[self.vertices[vertex].edges.index(i)]
                if direction != 1:
                    continue

            # If the node is not visited then recurse on it
            if not visited[i]:
                if self.is_cyclic_util(i, visited, rec_stack):
                    return True

            # If an adjacent vertex is visited and
            # not parent of current vertex, then there is a cycle
            elif rec_stack[i]:
                return True

        rec_stack[vertex] = False
        return False

    def is_cyclic(self):

        # Mark all the vertices as not visited
        visited = [False] * len(self.vertices)
        rec_stack = [False] * len(self.vertices)

        # Call the recursive helper function
        # to detect cycle in different DFS trees
        for i in range(len(self.vertices)):
            if not visited[i]:  # Don't recur for u if it is already visited
                if self.is_cyclic_util(i, visited, rec_stack):
                    return True

        return False

    def kosaraju_scc(self):
        """
        Finds strongly connected components in the given directed graph using Kosaraju's algorithm.

        Args:
        - graph (DirectedGraph): The directed graph for which to find SCCs.

        Returns:
        - List[List[int]]: A list of lists, where each inner list contains the indices of nodes
                        that form a strongly connected component.
        """
        stack = []
        visited = set()

        # Step 1: Fill vertices in stack according to their finishing times
        for vertex in self.vertices:
            if vertex.index not in visited:
                self.fill_order(vertex.index, visited, stack)

        # Step 2: Reverse graph
        reversed_graph = self.reverse_graph()

        # Step 3: Process all vertices in order defined by Stack
        visited.clear()
        sccs = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                scc = []
                self.dfs_util(reversed_graph, vertex, visited, scc)
                sccs.append(scc)

        return sccs

    def fill_order(self, v, visited, stack):
        """
        Utility function for DFS and to fill the stack with vertices based on their finishing times.

        Args:
        - graph (DirectedGraph): The graph to perform DFS on.
        - v (int): The starting vertex index for DFS.
        - visited (set): Set of visited vertices.
        - stack (list): Stack to push vertices according to their finishing times.
        """
        visited.add(v)

        # Assuming graph.vertices[v] provides direct access to the DirectedGraphNode by its index
        for i in self.vertices[v].edges:
            if i not in visited:
                self.fill_order(i, visited, stack)
        stack = stack.append(v)

    def reverse_graph(self):
        """
        Reverses the direction of all edges in the graph.

        Args:
        - graph (DirectedGraph): The graph to reverse.

        Returns:
        - DirectedGraph: A new graph with reversed edges.
        """
        reversed_graph = DirectedGraph()
        for vertex in range(len(self.vertices)):
          
            reversed_graph.add_vertex(vertex.data)

        for vertex in range(len(self.vertices)):
            for neighbor in self.vertices[vertex].edges:

                index = self.vertices[vertex].edges.index(neighbor)
                reversed_graph.add_edge(neighbor, vertex, self.vertices[vertex].directions[index])  # Reversing the edge direction

        return reversed_graph

    def dfs_util(self, reversed_graph, v, visited, scc):
        """
        A utility function for DFS traversal that tracks the strongly connected component.

        Args:
        - graph (DirectedGraph): The graph to perform DFS on.
        - v (int): The starting vertex index for DFS.
        - visited (set): Set of visited vertices.
        - scc (list): List to accumulate vertices in the current SCC.
        """
        visited.add(v)
        scc.append(v)

        # Assuming graph.vertices[v] provides direct access to the DirectedGraphNode by its index
        for i in self.vertices[v].edges:
            if i not in visited:
                self.dfs_util(reversed_graph, i, visited, scc)


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
        if v == self.vertices[u].edges[-1] and \
                len(self.vertices[u].edges) > \
                len(self.vertices[u].directions):
            self.vertices[u].directions.append(direction)
        else:
            self.vertices[u].directions[self.vertices[u].edges.index(v)] = \
                direction

    def add_direction_back(self, u: int, v: int, direction: int = 0):

        # from v to u
        if u == self.vertices[v].edges[-1] and \
                len(self.vertices[v].edges) > \
                len(self.vertices[v].directions):
            self.vertices[v].directions.append(-direction)
        else:
            self.vertices[v].directions[self.vertices[v].edges.index(u)] = \
                -direction

    def remove_edge(self, u: int, v: int):
        if v in self.vertices[u].edges:
            del self.vertices[u].directions[self.vertices[u].edges.index(v)]
        if u in self.vertices[v].edges:
            del self.vertices[v].directions[self.vertices[v].edges.index(u)]
        super().remove_edge(u, v)

    def calculate_element(self, vertex, neighbor):
        return self.vertices[vertex].directions[
            self.vertices[vertex].edges.index(neighbor)]

    def topological_sort_util(self, vertex, visited, stack):

        visited[vertex] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.vertices[vertex].edges:
            # Check if the edge direction allows moving from v to i
            index = self.vertices[vertex].edges.index(i)
            if not visited[i] and \
                    self.vertices[vertex].directions[index] == 1:
                self.topological_sort_util(i, visited, stack)

        # Push current vertex to stack which stores the result
        stack.insert(0, vertex)

    def topological_sort(self):

        # Step 1: Check for cycles
        if self.is_cyclic():
            raise RecursionError(
                "The graph has a cycle. Topological sort not possible.")

        # Step 2: Perform Topological Sort
        visited = [False] * len(self.vertices)
        stack = []

        for i in range(len(self.vertices)):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        return stack

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

            direction = self.vertices[vertex]\
                .directions[self.vertices[vertex].edges.index(neighbor)]
            if direction != 1:
                continue
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
        # on the current dfs have their indexes
        # and we can start to search for nodes in the current scc segment

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

        logging.info(str(low_link) + ' ' + str(scc))

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

        if v == self.vertices[u].edges[-1] and \
                len(self.vertices[u].edges) > \
                len(self.vertices[u].weights):
            self.vertices[u].weights.append(u_to_v_weight)
        else:
            self.vertices[u].weights[self.vertices[u].edges.index(v)] = \
                u_to_v_weight

        if u_to_v_weight < 0:
            self.negative_edge_weight = True

    def add_weight_back(self, u: int, v: int, v_to_u_weight: float = 0):

        if u == self.vertices[v].edges[-1] and \
                len(self.vertices[v].edges) > \
                len(self.vertices[v].weights):
            self.vertices[v].weights.append(v_to_u_weight)
        else:
            self.vertices[v].weights[self.vertices[v].edges.index(u)] = \
                v_to_u_weight

        if v_to_u_weight < 0:
            self.negative_edge_weight = True

    def remove_edge(self, u: int, v: int):
        if v in self.vertices[u].edges:
            del self.vertices[u].weights[self.vertices[u].edges.index(v)]
        if u in self.vertices[v].edges:
            del self.vertices[v].weights[self.vertices[v].edges.index(u)]
        super().remove_edge(u, v)

    def calculate_element(self, vertex, neighbor):
        return self.vertices[vertex].directions[
            self.vertices[vertex].edges.index(neighbor)] * \
            self.vertices[vertex].weights[
            self.vertices[vertex].edges.index(neighbor)]

    def dijkstra(self, start):

        if self.negative_edge_weight:
            raise ValueError("Dijkstra's algorithm does not work on " +
                             "graphs where negative_edge_weight exists")

        self._dijkstra(start)
