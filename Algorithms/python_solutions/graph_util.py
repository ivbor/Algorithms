from typing import Any
from collections import deque


def reconstruct_path(src: int, target: int, parent: list[int]) -> list[int]:
    """
    Function to reconstruct path from source to target using parent array.

    Parameters
    ----------
    src: int
        Index of starting vertex.

    target: int
        Index of the target vertex.

    parent: list[int]
        List where each vertex's index, being the index of the list,
        has its parent, index of vertex from which it was visited first,
        being the value in the list.

    Returns
    -------
    list[int]
        Path from the start vertex to the target, including both.
    """
    path = []
    while target != -1:
        path.append(target)
        target = parent[target]
    path.reverse()
    return path if path[0] == src else []


class Graph_util:
    """
    Class storing utility methods for the main graph class.

    Methods
    -------
    _find_arg(self, default: Any, arg_dict: dict[int, str], *args, **kwargs)
        -> Any
        Method for finding arg among args and kwargs provided.

    _find_index(self, **kwargs) -> int | None
        Method finding index of the vertex to remove among kwargs by data or
        index.

    is_cyclic_util(self, vertex: int,
                   visited: list[bool], rec_stack: list[bool]) -> bool
        Utility method which is used by is cyclic method.

    topological_sort_util(self, vertex: int,
                          visited: list[bool], stack: list[int]) -> None
        Utility method which is used by topological sort method.

    tarjan_dfs(self, vertex: int, index: list[int],
               stack: list[int], low_link: list[int], on_stack: list[bool],
               scc: list[list[int]]) -> None
        Utility method which is used by tarjan_scc method.

    fill_order(self, vertex: int, visited: set[int],
               stack: list[int]) -> None
        Utility function for DFS and to fill the stack with vertices
        based on their finishing times.

    bfs_level_graph(self, source: int) -> list[int]:
        A method to set up levels for vertices for Dinic's algorithms
        using BFS.

    dfs_blocking_flow(self, source: int, sink: int, flow: int,
                          levels: list[int]) -> int:
        Performs DFS to find a blocking flow in a level graph
        from source to sink.

    initialize_preflow(self, source: int) -> None:
        Initializes heights and preflows for all vertices
        for Goldberg-Tarjan's flow calculation algorithm.

    push_flow(self, u: int, v: int) -> bool:
        A method to push flow from vertex with index u
        to the vertex with index v if push is possible.

    lift_vertex(self, u: int) -> None:
        Increase vertex height by 1.

    discharge_excess_flow(self, u: int) -> None:
        Discharge excess flow down the path to the sink from the vertex.

    """

    def _find_arg(self, default: Any,
                  arg_dict: dict[int, str], *args, **kwargs) -> Any:
        """
        Find the required argument among args.

        Parameters
        ----------
        default: Any
            Value to be returned if the required argument was not provided.

        arg_dict: dict[int, str]
            Dictionary where index corresponds to the possible argument
            position in args, and value - in kwargs.

        Returns
        -------
        Any
            The required argument found within args or kwargs or the default
            value if the argument was not found.
        """

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

    def _find_index(self, **kwargs) -> int | None:
        """
        Find index of the vertex by data or index provided in kwargs
        for further removal.

        Parameters
        ----------
        kwargs['index']: int
            Index of the vertex to remove.
        or
        kwargs['data']: Any
            Data inside the vertex to remove.

        Returns
        -------
        int
            The index of the vertex to remove.

        Raises
        ------
        KeyError
            If data or index were not found among kwargs.
        """

        if 'data' in kwargs.keys():
            index = \
                [vertex.index for vertex in self.vertices
                 if vertex.data == kwargs['data']][0]
        elif 'index' in kwargs.keys():
            index = kwargs['index']
        else:
            raise KeyError('no index or data specified to remove')
        return index

    def is_cyclic_util(self, vertex: int,
                       visited: list[bool], rec_stack: list[bool]) -> bool:
        """
        Utility method which is used by is cyclic method.

        Parameters
        ----------
        vertex: int
            Vertex being visited.

        visited: list[bool]
            List where vertices are marked as visited (True)
            or not visited (False).

        rec_stack: list[bool]
            List used as a stack showing which vertices were visited
            in the active iteration of the is_cyclic method.

        Returns
        -------
        bool
            Whether the cycle was discovered during current iteration.
        """

        # Mark the current node as visited
        visited[vertex] = True
        # And put it on the stack
        rec_stack[vertex] = True

        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.vertices[vertex].edges.keys():

            # If the node is not visited then recurse on it
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, rec_stack):
                    return True

            # If an adjacent vertex is visited and
            # not parent of current vertex, then there is a cycle
            elif rec_stack[neighbor]:
                return True

        # Remove current vertex from the stack after the visit
        rec_stack[vertex] = False
        return False

    def topological_sort_util(self, vertex: int,
                              visited: list[bool], stack: list[int]) -> None:
        """
        Utility method which is used by topological sort method.

        Parameters
        ----------
        vertex: int
            Vertex for which the place is being searched.

        visited: list[bool]
            List where vertices are marked as visited (True)
            or not visited (False).

        stack: list[int]
            List which stores the result of the sort.

        Returns
        -------
        None
        """

        visited[vertex] = True

        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.vertices[vertex].edges.keys():
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)

        # Push current vertex to the stack which stores the result
        stack.insert(0, vertex)

    def tarjan_dfs(self, vertex: int, index: list[int], stack: list[int],
                   low_link: list[int], on_stack: list[bool],
                   scc: list[list[int]]) -> None:
        """
        Utility method which is used by tarjan_scc method.

        Parameters
        ----------
        vertex: int
            Vertex being visited.

        index: list[int]
            List where all vertices are assigned an index based on
            how early they were visited or -1 if they have not been visited.

        stack: list[int]
            List gathering current scc segment.

        low_link: list[int]
            List where all vertices are assigned a low-link value based on
            the smallest index of visited vertex from which the current
            one is accessible. Unvisited are assigned -1's.

        on_stack: list[bool]
            List showing which vertices are visited in the current dfs queue.

        scc: list[list[int]]
            List of sccs.

        Returns
        -------
        None
        """

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

        for neighbor in self.vertices[vertex].edges.keys():

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

    def fill_order(self, vertex: int,
                   visited: set[int], stack: list[int]) -> None:
        """
        Utility function for DFS and to fill the stack with vertices
        based on their finishing times.

        Parameters
        ----------
        vertex: int
            Currently visited vertex.

        visited: set
            Set of visited vertices.

        stack: list[int]
            Stack to push vertices according to their finishing times.

        Returns
        -------
        None
        """

        visited.add(vertex)

        for neighbor in self.vertices[vertex].edges.keys():
            if neighbor not in visited:
                self.fill_order(neighbor, visited, stack)
        stack.append(vertex)

    def bfs_level_graph(self, source: int) -> list[int]:
        """
        A method to set up levels for vertices for Dinic's algorithms
        using BFS.

        Parameters
        ----------
        source: int
            Vertex which is the source of the flow.

        Returns
        -------
        list[int]
            The list of levels of vertices where indexes are ones of vertices
            and values are levels.
        """

        levels = [-1] * len(self.vertices)
        levels[source] = 0
        queue = deque([source])
        while queue:
            vertex = queue.popleft()
            for _, edge in self.vertices[vertex].edges.items():
                # Check capacity and if the level is set
                if edge.capacity - edge.flow > 0 and \
                        levels[edge.second_node] < 0:
                    levels[edge.second_node] = levels[vertex] + 1
                    queue.append(edge.second_node)
        return levels

    def dfs_blocking_flow(self, source: int, sink: int, flow: int,
                          levels: list[int]) -> int:
        """
        Performs DFS to find a blocking flow in a level graph
        from source to sink.

        Parameters
        ----------
        source : int
            The index of the source vertex from where the flow starts.

        sink : int
            The index of the sink vertex where the flow ends.

        flow : int
            The amount of flow that can potentially be pushed through
            the path.

        levels : list[int]
            A list representing the level graph
            where levels[i] is the level of vertex i.

        Returns
        -------
        int or float
            The amount of flow that was actually pushed
            from the source to the sink.
            If no flow is possible, returns 0.

        Raises
        ------
        KeyError
            If a reverse edge necessary for updating flow does not exist,
            indicating an inconsistency in the graph's edge management.
        """

        if source == sink:
            return flow
        for _, edge in self.vertices[source].edges.items():
            remaining_capacity = edge.capacity - edge.flow
            if remaining_capacity > 0 \
                    and levels[edge.second_node] == levels[source] + 1:
                # Min flow in path
                path_flow = min(flow, remaining_capacity)
                result_flow = \
                    self.dfs_blocking_flow(edge.second_node, sink,
                                           path_flow, levels)
                if result_flow > 0:
                    # Update capacities in the direction TO the sink
                    edge.flow += result_flow
                    # and FROM the sink
                    if source in [i for i in self.vertices[edge.second_node]
                                                 .edges.keys()]:
                        self.vertices[edge.second_node].edges[source]\
                            .flow -= result_flow
                    else:
                        raise KeyError(
                            f'no reverse edge from {edge.second_node} to \
                            {source}')
                    return result_flow
        return 0

    def initialize_preflow(self, source: int) -> None:
        """
        Initializes heights and preflows for all vertices
        for Goldberg-Tarjan's flow calculation algorithm.

        Parameters
        ----------
        source : int
            The index of the source vertex in the graph.

        Returns
        -------
        None
        """
        # Height initialization
        for vertex in self.vertices.keys():
            self.vertices[vertex].height = 0
            self.vertices[vertex].excess_flow = 0
        self.vertices[source].height = len(self.vertices)

        # Preflow initialization
        for edge in self.vertices[source].edges.keys():
            # Send max flow
            self.vertices[source].edges[edge].flow = \
                self.vertices[source].edges[edge].capacity
            self.vertices[edge].excess_flow += \
                self.vertices[source].edges[edge].flow
            self.vertices[source].excess_flow -= \
                self.vertices[source].edges[edge].flow

    def push_flow(self, u: int, v: int) -> bool:
        """
        A method to push flow from vertex with index u
        to the vertex with index v if push is possible.

        Parameters
        ----------
        u: int
            The index of the vertex to push from.

        v: int
            The index of the vertex to push to.

        Returns
        -------
        bool
            Whether it was possible to push flow.
        """
        edge = self.vertices[u].edges[v]
        flow = min(self.vertices[u].excess_flow,
                   edge.capacity - edge.flow)
        if flow > 0 and \
                self.vertices[u].height == self.vertices[v].height + 1:
            self.vertices[u].edges[v].flow += flow
            self.vertices[u].excess_flow -= flow
            self.vertices[v].excess_flow += flow
            return True
        return False

    def lift_vertex(self, u: int) -> None:
        """
        Increase vertex height by 1.

        Parameters
        ----------
        u: int
            The index of the vertex which height will be increased.

        Returns
        -------
        None
        """
        min_height = float('inf')
        for edge in self.vertices[u].edges.keys():
            if self.vertices[u].edges[edge].capacity > \
                    self.vertices[u].edges[edge].flow:
                min_height = \
                    min(min_height, self.vertices[edge].height)
        if min_height < float('inf'):
            self.vertices[u].height = min_height + 1

    def discharge_excess_flow(self, u: int) -> None:
        """
        Discharge excess flow down the path to the sink from the vertex.

        Parameters
        ----------
        u: int
            The vertex from which excess flow will be discharged.

        Returns
        -------
        None
        """
        while self.vertices[u].excess_flow > 0:
            for neighbor in self.vertices[u].edges.keys():
                if self.push_flow(u, neighbor):
                    break
            else:
                # No push occurred, lift the vertex
                self.lift_vertex(u)
                # Necessary to prevent infinite loop if no push is possible
                break
