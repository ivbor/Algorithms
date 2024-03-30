from Algorithms.python_solutions.undirected_graph import UndirectedGraph
from Algorithms.python_solutions.graph_nodes import DirectedGraphNode


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
        - List[List[int]]: A list of lists, where each inner list contains
        the indices of nodes that form a strongly connected component.
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
