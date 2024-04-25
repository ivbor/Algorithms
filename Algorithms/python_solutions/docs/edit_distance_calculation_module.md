# edit_distance_calculation_module

This module provides functions to calculate the edit distance between two
strings using different distance metrics. It includes functions for Hamming
distance, Jaro similarity, and uses the Longest Common Subsequence and
Damerau-Levenshtein distance algorithms for more complex edit distance
calculations.

Functions
---------
edit_distance(str1: str, str2: str, distance: str = 'dl') -> float
    Compute the edit distance between two strings using a specified distance
    metric.

hamming_distance(str1: str, str2: str) -> int
    Calculate the Hamming distance between two strings.

jaro_distance(str1: str, str2: str) -> float
    Calculate the Jaro similarity between two strings.

<a id="python_solutions.edit_distance.LongestCommonSubsequence"></a>

## LongestCommonSubsequence

<a id="python_solutions.edit_distance.DamerauLevensteinDistance"></a>

## DamerauLevensteinDistance

<a id="python_solutions.edit_distance.edit_distance"></a>

#### edit\_distance

```python
def edit_distance(str1, str2, distance='dl')
```

Compute the edit distance between two strings.

This function calculates the edit distance between two input strings
using one of the available distance metrics. You can choose the
- **following metrics**: Jaro, Hamming, LongestCommonSubsequence or

DamerauLevensteinDistance.

DamerauLevensteinDistance is the most universal of them.
Jaro distance can be the metric for the distance between the strings
containing matching and transposing characters.
LongestCommonSubsequence distance is a metric for edit distance, using
the length of LCS of the strings.
Hamming distance works only for the strings with the same length and
share a large share of characters (including their positions), e.g.
'karoline' and 'kathrine'.

## Parameters
- **str1**: str

    The first input string.

- **str2**: str

    The second input string.

- **distance**: str, optional

    The distance metric to use. Possible values are
    'jaro' for Jaro distance,
    'hamming' for Hammimg distance,
    'lcs' for distance based on the LongestCommonSubsequence or
    'dl' for DamerauLevensteinDistance.
    Default is 'dl'.

## Returns

float
    The computed edit distance based on the selected distance metric.

## Raises

ValueError
    Raised if the distance is 'hamming' and the input strings have
    different lengths.

<a id="python_solutions.edit_distance.hamming_distance"></a>

#### hamming\_distance

```python
def hamming_distance(str1, str2)
```

Calculate the Hamming distance between two strings.

The Hamming distance is the number of positions at which the
corresponding elements in the input strings of the same length are
different.

## Parameters
- **str1**: str

    The first input string.

- **str2**: str

    The second input string.

## Returns

int
    The Hamming distance between the two input strings.

## Raises

ValueError
    Raised if the input strings have different lengths.

<a id="python_solutions.edit_distance.jaro_distance"></a>

#### jaro\_distance

```python
def jaro_distance(str1, str2)
```

Calculate the Jaro similarity between two strings.

The Jaro similarity measures the similarity between two strings.
A higher value indicates more similarity between the strings.
- **The general formula looks the following way**: d = (matches / length1 + matches / length2 + (matches - transpositions)

/ matches) / 3, where
matches are matches of the characters in the strings if they are not
not farther than int(max(length1, length2) / 2) - 1 characters apart,
length1 and length2 are lengths of the first and the second strings
accordingly,
transpositions is the number of matching characters that are not in the
right order.

## Parameters
- **str1**: str

    The first input string.

- **str2**: str

    The second input string.

## Returns

float
    The Jaro similarity between the two input strings.

<a id="python_solutions.graph.heapq"></a>

## heapq

<a id="python_solutions.graph.logging"></a>

## logging

<a id="python_solutions.graph.deque"></a>

## deque

<a id="python_solutions.graph.GraphNode"></a>

## GraphNode

<a id="python_solutions.graph.Edge"></a>

## Edge

<a id="python_solutions.graph.VerticesList"></a>

## VerticesList Objects

```python
class VerticesList(dict)
```

<a id="python_solutions.graph.VerticesList.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

<a id="python_solutions.graph.VerticesList.append"></a>

#### append

```python
def append(__object) -> None
```

<a id="python_solutions.graph.VerticesList.__getitem__"></a>

#### \_\_getitem\_\_

```python
def __getitem__(index)
```

<a id="python_solutions.graph.VerticesList.__iter__"></a>

#### \_\_iter\_\_

```python
def __iter__()
```

<a id="python_solutions.graph.VerticesList.__delitem__"></a>

#### \_\_delitem\_\_

```python
def __delitem__(index)
```

<a id="python_solutions.graph.Graph"></a>

## Graph Objects

```python
class Graph()
```

<a id="python_solutions.graph.Graph.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

<a id="python_solutions.graph.Graph.all_vertices"></a>

#### all\_vertices

```python
def all_vertices()
```

<a id="python_solutions.graph.Graph.add_vertex"></a>

#### add\_vertex

```python
def add_vertex(*args, **kwargs)
```

<a id="python_solutions.graph.Graph._find_arg"></a>

#### \_find\_arg

```python
def _find_arg(default, arg_dict: dict[int, str], *args, **kwargs)
```

<a id="python_solutions.graph.Graph._find_index"></a>

#### \_find\_index

```python
def _find_index(**kwargs)
```

<a id="python_solutions.graph.Graph.remove_vertex"></a>

#### remove\_vertex

```python
def remove_vertex(**kwargs)
```

<a id="python_solutions.graph.Graph.add_edge"></a>

#### add\_edge

```python
def add_edge(u: int, v: int, *args, **kwargs)
```

<a id="python_solutions.graph.Graph.remove_edge"></a>

#### remove\_edge

```python
def remove_edge(u: int, v: int)
```

<a id="python_solutions.graph.Graph.bfs"></a>

#### bfs

```python
def bfs(start, target=None)
```

<a id="python_solutions.graph.Graph.to_adjacency_matrix"></a>

#### to\_adjacency\_matrix

```python
def to_adjacency_matrix()
```

<a id="python_solutions.graph.Graph.calculate_element"></a>

#### calculate\_element

```python
def calculate_element(vertex, neighbor)
```

<a id="python_solutions.graph.Graph.topological_sort_util"></a>

#### topological\_sort\_util

```python
def topological_sort_util(vertex, visited, stack)
```

<a id="python_solutions.graph.Graph.topological_sort"></a>

#### topological\_sort

```python
def topological_sort()
```

<a id="python_solutions.graph.Graph.tarjan_dfs"></a>

#### tarjan\_dfs

```python
def tarjan_dfs(vertex, index, stack, low_link, on_stack, scc)
```

<a id="python_solutions.graph.Graph.scc"></a>

#### scc

```python
def scc()
```

<a id="python_solutions.graph.Graph.kosaraju_scc"></a>

#### kosaraju\_scc

```python
def kosaraju_scc()
```

Finds strongly connected components in the given directed graph
using Kosaraju's algorithm.

- **Args**: - graph (DirectedGraph): The directed graph for which to find SCCs.


- **Returns**: - List[List[int]]: A list of lists, where each inner list contains

the indices of nodes that form a strongly connected component.

<a id="python_solutions.graph.Graph.fill_order"></a>

#### fill\_order

```python
def fill_order(vertex, visited, stack)
```

Utility function for DFS and to fill the stack with vertices
based on their finishing times (meaning the time when all not visited
vertices accessible from this vertex by transitions with direction 1
become visited).

- **Args**: - graph (DirectedGraph): The graph to perform DFS on.

- vertex (int): The starting vertex index for DFS.
- visited (set): Set of visited vertices.
- stack (list): Stack to push vertices according to their
finishing times.

<a id="python_solutions.graph.Graph.reverse_graph"></a>

#### reverse\_graph

```python
def reverse_graph()
```

Reverses the direction of all edges in the graph.

- **Args**: - graph (DirectedGraph): The graph to reverse.


- **Returns**: - DirectedGraph: A new graph with reversed edges.


<a id="python_solutions.graph.Graph.dfs_util"></a>

#### dfs\_util

```python
def dfs_util(reversed_graph, vertex, visited, scc)
```

A utility function for DFS traversal that tracks
the strongly connected component.

- **Args**: - graph (DirectedGraph): The graph to perform DFS on.

- vertex (int): The starting vertex index for DFS.
- visited (set): Set of visited vertices.
- scc (list): List to accumulate vertices in the current SCC.

<a id="python_solutions.graph.Graph.dijkstra"></a>

#### dijkstra

```python
def dijkstra(start: int)
```

<a id="python_solutions.graph.Graph.is_cyclic_util"></a>

#### is\_cyclic\_util

```python
def is_cyclic_util(vertex, visited, rec_stack)
```

<a id="python_solutions.graph.Graph.is_cyclic"></a>

#### is\_cyclic

```python
def is_cyclic()
```

<a id="python_solutions.graph.Graph.bellman_ford"></a>

#### bellman\_ford

```python
def bellman_ford(start)
```

<a id="python_solutions.graph.Graph.bfs_level_graph"></a>

#### bfs\_level\_graph

```python
def bfs_level_graph(source)
```

<a id="python_solutions.graph.Graph.dfs_blocking_flow"></a>

#### dfs\_blocking\_flow

```python
def dfs_blocking_flow(source, sink, flow, levels)
```

<a id="python_solutions.graph.Graph.dinics_algorithm"></a>

#### dinics\_algorithm

```python
def dinics_algorithm(source, sink)
```

<a id="python_solutions.graph.Graph.initialize_preflow"></a>

#### initialize\_preflow

```python
def initialize_preflow(source)
```

<a id="python_solutions.graph.Graph.push_flow"></a>

#### push\_flow

```python
def push_flow(u, v)
```

<a id="python_solutions.graph.Graph.lift_vertex"></a>

#### lift\_vertex

```python
def lift_vertex(u)
```

<a id="python_solutions.graph.Graph.discharge_excess_flow"></a>

#### discharge\_excess\_flow

```python
def discharge_excess_flow(u)
```

<a id="python_solutions.graph.Graph.goldberg_tarjan"></a>

#### goldberg\_tarjan

```python
def goldberg_tarjan(source, sink)
```

<a id="python_solutions.graph.Graph.color_vertices"></a>

#### color\_vertices

```python
def color_vertices()
```

<a id="python_solutions.graph.Graph.all_edges"></a>

#### all\_edges

```python
def all_edges()
```

<a id="python_solutions.graph.Graph.color_edges"></a>

#### color\_edges

```python
def color_edges()
```

<a id="python_solutions.graph_nodes.BaseGraphNode"></a>

## BaseGraphNode Objects

```python
class BaseGraphNode()
```

<a id="python_solutions.graph_nodes.BaseGraphNode.__init__"></a>

#### \_\_init\_\_

```python
def __init__(index, data, color) -> None
```

<a id="python_solutions.graph_nodes.BaseGraphNode.__str__"></a>

#### \_\_str\_\_

```python
def __str__() -> str
```

<a id="python_solutions.graph_nodes.BaseGraphNode.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="python_solutions.graph_nodes.GraphNode"></a>

## GraphNode Objects

```python
class GraphNode(BaseGraphNode)
```

<a id="python_solutions.graph_nodes.GraphNode.__init__"></a>

#### \_\_init\_\_

```python
def __init__(index, data, edges=[], capacities=[], color=0) -> None
```

<a id="python_solutions.graph_nodes.WeightedGraphNode"></a>

## WeightedGraphNode Objects

```python
class WeightedGraphNode(GraphNode)
```

<a id="python_solutions.graph_nodes.WeightedGraphNode.__init__"></a>

#### \_\_init\_\_

```python
def __init__(index,
             data,
             edges=[],
             weights=[],
             capacities=[],
             color=0) -> None
```

<a id="python_solutions.graph_nodes.Edge"></a>

## Edge Objects

```python
class Edge()
```

<a id="python_solutions.graph_nodes.Edge.__init__"></a>

#### \_\_init\_\_

```python
def __init__(first_node: int,
- **second_node**: int,

             weight=1,
             capacity=0,
             flow=0,
             color=0,
             *args,
             **kwargs) -> None
```