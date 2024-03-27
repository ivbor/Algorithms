import logging
import copy
import heapq


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
            raise KeyError('for each edge a direction (0 or 1) ' +
                           'must be specified')
        if any(direction < 0 for direction in directions):
            raise ValueError('direction can only be 0 or 1')
        super().__init__(index, data, edges)
        self.directions = copy.deepcopy(directions)


class WeightedGraphNode(DirectedGraphNode):

    def __init__(self, index, data,
                 edges=[], directions=[], weights=[]) -> None:
        if len(edges) != len(weights):
            raise KeyError('for each edge a weight must be specified')
        super().__init__(index, data, edges, directions)
        self.weights = copy.deepcopy(weights)


class VerticesList(dict):

    def __init__(self):
        super().__init__()

    def append(self, __object) -> None:
        self[len(self)] = __object

    def __getitem__(self, index):
        if index not in self.keys():
            raise IndexError(f'there is no index {index} in the list')
        return dict.get(self, index)

    def __iter__(self):
        for elt in self.values():
            yield elt

    def __delitem__(self, index):
        dict.__delitem__(self, index)


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
            present_indexes = \
                [i for i in self.vertices.keys()]
            missing_vals = set(present_indexes).difference(
                            set([i for i in range(max(present_indexes) + 1)]))
            if len(missing_vals) != 0:
                index = min(missing_vals)
            else:
                index = max(present_indexes) + 1
        new_node = self.node_type(index, *args, **kwargs)
        self.vertices[index] = new_node
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
            index = \
                [vertex.index for vertex in self.vertices
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

    def remove_edge(self, u: int, v: int):
        if v in self.vertices[u].edges:
            self.vertices[u].edges.remove(v)

    def bfs(self, start, target=None):

        to_return = []
        visited = [False] * (
            max([vertex.index for vertex in self.vertices]) + 1)
        predecessor = [None] * (
            max([vertex.index for vertex in self.vertices]) + 1)
        current_row = [start]
        visited[start] = True

        while len(current_row) != 0:
            vertex = current_row[0]
            current_row = current_row[1:]
            if target is not None:
                if vertex == target:
                    current = target
                    while current is not None:
                        to_return.append(current)
                        current = predecessor[current]
                    return to_return[::-1]
            for neighbor in self.vertices[vertex].edges:
                if not visited[neighbor]:
                    current_row.append(neighbor)
                    visited[neighbor] = True
                    predecessor[neighbor] = vertex
        if target is not None:
            raise IndexError(
                f'there is no path between {start} and {target}')

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
        return 1

    def _dijkstra(self, start: int):

        # Initialize distances to all nodes as infinity
        distances = \
            [float('inf') for _ in self.vertices]
        # Set distance to start node as 0
        distances[start] = 0
        # Priority queue to store nodes to visit
        priority_queue = [(0, start)]
        current_distances = {start: 0}

        while priority_queue:
            logging.info('1')
            # Pop the node with the smallest distance from the priority queue
            current_distance, current_node = heapq.heappop(priority_queue)
            logging.info(len(priority_queue))
            # If the current distance is greater than the recorded distance,
            # skip
            if current_distance > distances[current_node]:
                logging.info('3')
                continue

            # Visit each neighbor of the current node
            for neighbor in self.vertices[current_node].edges:
                logging.info('4')
                distance = current_distance + \
                    self.calculate_element(current_node, neighbor)
                # If the new distance is shorter,
                # update it and add to the priority queue
                if distance < distances[neighbor]:
                    logging.info('5')
                    distances[neighbor] = distance
                    current_distances[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))
                logging.info('6')

        return distances  # , current_distances

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

    def bellman_ford(self, start):
        # Step 1: Initialize distances from src to all other vertices as INFINITE and src to itself as 0. Also, create a parent array to store the shortest path tree
        dist = [float("Inf")] * len(self.vertices) 
        dist[start] = 0
        parent = [-1] * len(self.vertices)  # Parent array to store the path
        
        # Step 2: Relax all edges |V| - 1 times
        for _ in range(len(self.vertices) - 1):
            for vertex in self.vertices:
                for neighbor in vertex.edges:
                    if dist[vertex.index] != float("Inf") and dist[vertex.index] + self.calculate_element(vertex.index, neighbor) < dist[neighbor]:
                        dist[neighbor] = dist[vertex.index] + self.calculate_element(vertex.index, neighbor)
                        parent[neighbor] = vertex.index

        # Step 3: Check for negative-weight cycles
        for vertex in self.vertices:
            for neighbor in vertex.edges:
                if dist[vertex.index] != float("Inf") and dist[vertex.index] + self.calculate_element(vertex.index, neighbor) < dist[neighbor]:
                    print("Graph contains negative weight cycle")
                    return None, None

        # Function to reconstruct path from source to j using parent array
        def reconstruct_path(src, j, parent):
            path = []
            while j != -1:
                path.append(j)
                j = parent[j]
            path.reverse()
            return path if path[0] == src else []

        # Reconstruct paths from src to all other vertices
        paths = {vertex.index: reconstruct_path(start, v, parent) for v in self.vertices}
        
        return dist, paths


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
            self.add_direction(u, v, directions[kwargs['nr']])
        else:
            self.add_direction(u, v, directions) 

    def add_direction(self, u: int, v: int, direction: int = 0):

        if direction < 0:
            raise ValueError('direction cannot be less than 0')
        # from u to v
        if v == self.vertices[u].edges[-1] and \
                len(self.vertices[u].edges) > \
                len(self.vertices[u].directions):
            self.vertices[u].directions.append(direction)
        else:
            self.vertices[u].directions[self.vertices[u].edges.index(v)] = \
                direction

    def remove_edge(self, u: int, v: int):
        if v in self.vertices[u].edges:
            del self.vertices[u].directions[self.vertices[u].edges.index(v)]
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

    def kosaraju_scc(self):
        """
        Finds strongly connected components in the given directed graph
        using Kosaraju's algorithm.

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

    def fill_order(self, vertex, visited, stack):
        """
        Utility function for DFS and to fill the stack with vertices
        based on their finishing times (meaning the time when all not visited
        vertices accessible from this vertex by transitions with direction 1
        become visited).

        Args:
        - graph (DirectedGraph): The graph to perform DFS on.
        - vertex (int): The starting vertex index for DFS.
        - visited (set): Set of visited vertices.
        - stack (list): Stack to push vertices according to their
        finishing times.
        """

        visited.add(vertex)

        for neighbor in self.vertices[vertex].edges:
            direction = self.vertices[vertex]\
                .directions[self.vertices[vertex].edges.index(neighbor)]
            if direction != 1:
                continue
            if neighbor not in visited:
                self.fill_order(neighbor, visited, stack)
        stack.append(vertex)

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
            reversed_graph.add_vertex(data=self.vertices[vertex].data)

        for vertex in self.vertices:
            for neighbor, direction in zip(vertex.edges,
                                           vertex.directions):

                reversed_graph.add_edge(neighbor, vertex.index, direction)
                # Reversing the edge direction

        return reversed_graph

    def dfs_util(self, reversed_graph, vertex, visited, scc):
        """
        A utility function for DFS traversal that tracks
        the strongly connected component.

        Args:
        - graph (DirectedGraph): The graph to perform DFS on.
        - vertex (int): The starting vertex index for DFS.
        - visited (set): Set of visited vertices.
        - scc (list): List to accumulate vertices in the current SCC.
        """
        visited.add(vertex)
        scc.append(vertex)

        for neighbor in reversed_graph.vertices[vertex].edges:
            direction = reversed_graph.vertices[vertex]\
                .directions[reversed_graph.vertices[vertex]
                            .edges.index(neighbor)]
            if direction != 1:
                continue
            if neighbor not in visited:
                self.dfs_util(reversed_graph, neighbor, visited, scc)


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
            self.add_weight(u, v, weights[0])
        elif len(weights) == 0:
            self.add_weight(u, v)

    def add_weight(self, u: int, v: int, u_to_v_weight: float = 0):

        if v == self.vertices[u].edges[-1] and \
                len(self.vertices[u].edges) > \
                len(self.vertices[u].weights):
            self.vertices[u].weights.append(u_to_v_weight)
        else:
            self.vertices[u].weights[self.vertices[u].edges.index(v)] = \
                u_to_v_weight

        if u_to_v_weight < 0:
            self.negative_edge_weight = True

    def remove_edge(self, u: int, v: int):
        if v in self.vertices[u].edges:
            del self.vertices[u].weights[self.vertices[u].edges.index(v)]
        super().remove_edge(u, v)

    def calculate_element(self, vertex, neighbor):
        index = self.vertices[vertex].edges.index(neighbor)
        return self.vertices[vertex].directions[index] * \
            self.vertices[vertex].weights[index]

    