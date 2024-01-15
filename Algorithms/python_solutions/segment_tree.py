"""
Segment Tree Module
===================

This module defines two classes, `SegmentTree` and `SegmentTreeOptimized`,
that implement a segment tree data structure.
A segment tree is a versatile data structure that allows for efficient
querying and updating of segments of an array.

Classes
-------
SegmentTree
    A class representing a segment tree.

SegmentTreeOptimized
    An optimized version of the segment tree class.

"""

from math import gcd
from typing import Callable


class SegmentTree(list):
    """
    A class representing a segment tree.

    Attributes
    ----------
    n: int
        The length of array on which SegmentTree is built.

    tree_size: int
        The size of the SegmentTree.

    tree_`action`: list[float]
        SegmentTrees for each distinct operation `action`.

    Methods
    -------
    __init__(self, arr: list) -> None
        Initializes a new instance of the `SegmentTree` class with
        the given array.

    build_tree(self, current_index: int, left: int, right: int) -> None
        Builds the segment tree using a recursive function.

    query(self, action: Callable, query_left: int, query_right: int) -> float
        Performs a query on the segment tree for the specified range
        (including query_left and query_right indexes) and action.

    _query(self, current_index: int, segment_left: int,
            segment_right: int, action: Callable, query_left: int,
            query_right: int) -> float
        Recursively performs a query on the segment tree.

    update(self, index: int, new_value: float) -> None
        Updates the value of a specified index in the segment tree.

    _update(self, current_index: int, segment_left: int, segment_right: int,
            index: int, new_value: float) -> None
        Recursively updates the value of a specified index in the segment
        tree.

    """

    def __init__(self, arr: list[float]) -> None:
        """
        Initializes a new instance of the `SegmentTree` class with the given
        array.

        Parameters
        ----------
        arr: list[float]
            An array to built the SegmentTree on.

        Returns
        -------
        None

        """
        super().__init__(arr)
        self.n = len(arr)
        self.tree_size = 2 ** (self.n - 1).bit_length() << 1
        self.tree_sum = [0] * self.tree_size
        self.tree_min = [float('inf')] * self.tree_size
        self.tree_max = [-float('inf')] * self.tree_size
        self.tree_gcd = [0] * self.tree_size

        # Build the segment tree using recursive function
        self.build_tree(0, 0, self.n - 1)

    def build_tree(self, current_index: int, left: int, right: int) -> None:
        """
        Builds the segment tree using a recursive function.

        Parameters
        ----------
        current_index: int
            Index for which the function currently calculates actions.

        left_index: int
            Left border of the tree with root in current_index.

        right_index: int
            Right border of the tree with root in current_index.

        Returns
        -------
        None

        """

        if left == right:
            self.tree_sum[current_index] = self[left]
            self.tree_min[current_index] = self[left]
            self.tree_max[current_index] = self[left]
            self.tree_gcd[current_index] = self[left]
        else:
            mid = (left + right) // 2
            left_index = 2 * current_index + 1
            right_index = 2 * current_index + 2

            # Recursively build the left and right subtrees
            self.build_tree(left_index, left, mid)
            self.build_tree(right_index, mid + 1, right)

            # Combine values from left and right subtrees
            self.tree_sum[current_index] = sum([
                self.tree_sum[left_index], self.tree_sum[right_index]])
            self.tree_min[current_index] = min(
                self.tree_min[left_index],
                self.tree_min[right_index])
            self.tree_max[current_index] = max(
                self.tree_max[left_index],
                self.tree_max[right_index])
            self.tree_gcd[current_index] = gcd(
                self.tree_gcd[left_index], self.tree_gcd[right_index])

    def query(self, action: Callable, query_left: int, query_right: int) \
            -> float:
        """
        Performs a query on the segment tree for the specified range and
        action.

        Parameters
        ----------
        action: Callable
            Operation to query among available for the tree. If action is not
            among available (sum, min, max, gcd), raises an error.

        query_left: int
            Left border of the range, included in the query.

        query_right: int
            Right border of the range, included in the query.

        Returns
        -------
        float
            The result of the query.

        Raises
        ------
        KeyError
            If query is called to perform operation not among defined.

        """
        if action not in [sum, min, max, gcd]:
            raise KeyError(
                f'Tree for action {action} not found. ' +
                'Trees available only for sum, min, max and gcd. ' +
                'If you need to add an action - use ' +
                'SegmentTreeOptimized class.')
        return self._query(0, 0, self.n - 1, action, query_left, query_right)

    def _query(self, current_index, segment_left, segment_right, action,
               query_left, query_right) -> float:
        """
        Recursively performs a query on the segment tree.

        Parameters
        ----------
        current_index: int
            Index for which the function currently calculates actions.

        segment_left: int
            Left border of the segment with root in current_index.

        segment_right: int
            Right border of the segment with root in current_index.

        action: Callable
            Operation to query among available for the tree.

        query_left: int
            Left border of the range, included in the query.

        query_right: int
            Right border of the range, included in the query.

        Returns
        -------
        float
            The result of the query.

        """

        if query_left <= segment_left and query_right >= segment_right:
            # Total overlap
            if action == sum:
                return self.tree_sum[current_index]
            elif action == min:
                return self.tree_min[current_index]
            elif action == max:
                return self.tree_max[current_index]
            elif action == gcd:
                return self.tree_gcd[current_index]
        if query_right < segment_left or query_left > segment_right:
            # No overlap
            if action in [gcd, sum]:
                return 0
            elif action == min:
                return float('inf')
            elif action == max:
                return -float('inf')

        mid = (segment_left + segment_right) // 2
        left_index = 2 * current_index + 1
        right_index = 2 * current_index + 2

        left_query = self._query(
            left_index,
            segment_left,
            mid,
            action,
            query_left,
            query_right)
        right_query = self._query(
            right_index,
            mid + 1,
            segment_right,
            action,
            query_left,
            query_right)

        if action == sum:
            return sum([left_query, right_query])
        else:  # action in [min, max, gcd]
            return action(left_query, right_query)

    def update(self, index: int, new_value: float) -> None:
        """
        Updates the value of a specified index in the segment tree.

        Parameters
        ----------
        index: int
            Index to update.

        new_value: float
            New value to assign to the specified index.

        Returns
        -------
        None

        """
        self._update(0, 0, self.n - 1, index, new_value)

    def _update(self, current_index: int, segment_left: int,
                segment_right: int, index: int, new_value: float) -> None:
        """
        Recursively updates the value of a specified index in the segment
        tree.

        Parameters
        ----------
        current_index: int
            Index for which the function currently calculates actions.

        segment_left: int
            Left border of the segment with root in current_index.

        segment_right: int
            Right border of the segment with root in current_index.

        index: int
            Index to update.

        new_value: float
            New value to assign to the specified index.

        Returns
        -------
        None

        """
        if segment_left == segment_right == index:
            self[index] = new_value
            self.tree_sum[current_index] = new_value
            self.tree_min[current_index] = new_value
            self.tree_max[current_index] = new_value
            self.tree_gcd[current_index] = new_value
            return

        mid = (segment_left + segment_right) // 2
        left_index = 2 * current_index + 1
        right_index = 2 * current_index + 2

        if index <= mid:
            self._update(left_index, segment_left, mid, index, new_value)
        else:
            self._update(right_index, mid + 1, segment_right,
                         index, new_value)

        self.tree_sum[current_index] = sum([
            self.tree_sum[left_index],
            self.tree_sum[right_index]])
        self.tree_min[current_index] = min(
            self.tree_min[left_index],
            self.tree_min[right_index])
        self.tree_max[current_index] = max(
            self.tree_max[left_index],
            self.tree_max[right_index])
        self.tree_gcd[current_index] = gcd(
            self.tree_gcd[left_index],
            self.tree_gcd[right_index])


class SegmentTreeOptimized:
    """
    An optimized version of the segment tree class.

    Attributes
    ----------
    n: int
        The length of array on which SegmentTree is built.

    tree_size: int
        The size of the SegmentTree.

    tree: list[list[float]]
        The main tree structure. Contains lists with the length equal to
        number of actions defined.

    action: list[Callable]
        A list where all defined operations are stored.

    arr: list[float]
        The list SegmentTreeOptimized is built on

    neutral: dict[Callable: float]
        The dict defining the neutral elements for each operation.

    Methods
    -------
    __init__(self, arr) -> None
        Initializes a new instance of the `SegmentTreeOptimized` class with
        the given array.

    determine_queries(self, left_index: int, right_index: int) ->
        tuple[Callable, Callable] | tuple[Callable, float] |
        tuple[float, float]
        Determines the queries for the left and right indices.

    build_tree(self, arr: list[float], current_index: int,
        left: int, right: int, action: Callable | None = None) -> None
        Builds the segment tree using a recursive function.

    query(self, action: Callable, query_left: int, query_right: int) -> float
        Performs a query on the segment tree for the specified range
        (including query_left and query_right indexes) and action.

    _query(self, current_index: int, segment_left: int,
        segment_right: int, action: Callable, query_left: int,
        query_right: int) -> float
        Recursively performs a query on the segment tree.

    update(self, index: int, new_value: float) -> None
        Updates the value of a specified index in the segment tree.

    _update(self, current_index: int, segment_left: int,
        segment_right: int, index: int, new_value: float) -> None
        Recursively updates the value of a specified index in the segment
        tree.

    new_action(self, func: Callable, neutral: float)
        Adds a new action to the segment tree and updates the
        tree accordingly.

    """

    def __init__(self, arr) -> None:
        """
        Initializes a new instance of the `SegmentTreeOptimized` class with
        the given array.

        Parameters
        ----------
        arr: list
            An array to build the SegmentTree on.

        Returns
        -------
        None

        """

        self.n = len(arr)
        self.tree_size = 2 ** (self.n - 1).bit_length() << 1
        self.tree = [None] * (self.tree_size)
        self.action = [sum, min, max, gcd]
        self.build_tree(arr, 0, 0, self.n - 1)
        self.arr = arr
        self.neutral = dict()

    # function reducing memory consumption from 8n to (5n - 4)
    def determine_queries(self, left_index, right_index) \
        -> tuple[Callable, Callable] | tuple[Callable, float] | \
            tuple[float, float]:
        """
        Determines the queries for the left and right indices.
        Its purpose is to give the same looking calls for the queries
        with only one element and with more than one element.

        Parameters
        ----------
        left_index: int
            The left index.

        right_index: int
            The right index.

        Returns
        -------
        left_query: Callable
            A lambda function representing the query for the left index.

        right_query: Callable
            A lambda function representing the query for the right index.

        """

        if isinstance(self.tree[left_index], list) and \
           isinstance(self.tree[right_index], list):
            def left_query(x): return self.tree[left_index][x]
            def right_query(x): return self.tree[right_index][x]
        elif isinstance(self.tree[left_index], list) and \
                isinstance(self.tree[right_index], int):
            def left_query(x): return self.tree[left_index][x]
            def right_query(x): return self.tree[right_index]
        elif isinstance(self.tree[left_index], int) and \
                isinstance(self.tree[right_index], int):
            def left_query(x): return self.tree[left_index]
            def right_query(x): return self.tree[right_index]

        return left_query, right_query

    def build_tree(self, arr: list, current_index: int, left: int,
                   right: int, action: Callable | None = None) -> None:
        """
        Builds the segment tree using a recursive function.

        Parameters
        ----------
        arr: list
            The array on which the SegmentTreeOptimized is built.

        current_index: int
            Index for which the function currently calculates action.

        left: int
            Left border of the tree with root in current_index.

        right: int
            Right border of the tree with root in current_index.

        action: Callable, optional
            Operation to query among available for the tree.

        Returns
        -------
        None

        """

        if left == right:
            self.tree[current_index] = arr[left]
        else:
            mid = (left + right) // 2
            left_index = 2 * current_index + 1
            right_index = 2 * current_index + 2

            self.build_tree(arr, left_index, left, mid, action=action)
            self.build_tree(arr, right_index, mid + 1, right, action=action)

            left_query, right_query = \
                self.determine_queries(left_index, right_index)

            if not isinstance(self.tree[current_index], list):
                self.tree[current_index] = \
                    [func([left_query(i), right_query(i)])
                     if func != gcd
                     else func(*[left_query(i), right_query(i)])
                     for i, func in enumerate(self.action)]
            else:
                index = self.action.index(action)
                self.tree[current_index].append(
                    action([left_query(index), right_query(index)]))

    def query(self, action: Callable, query_left: int, query_right: int) \
            -> float:
        """
        Performs a query on the segment tree for the specified range and
        action.

        Parameters
        ----------
        action: Callable
            Operation to query among available for the tree. If action is not
            among available, raises an error.

        query_left: int
            Left border of the range, included in the query.

        query_right: int
            Right border of the range, included in the query.

        Returns
        -------
        float
            The result of the query.
        """
        if action not in self.action:
            raise KeyError(
                f'Tree for action {action} not found. ' +
                f'Trees available only for {self.action}.')
        return self._query(0, 0, self.n - 1, action, query_left, query_right)

    def _query(self, current_index: int, segment_left: int,
               segment_right: int, action: Callable, query_left: int,
               query_right: int) -> float:
        """
        Recursively performs a query on the segment tree.

        Parameters
        ----------
        current_index: int
            Index for which the function currently calculates actions.

        segment_left: int
            Left border of the segment with root in current_index.

        segment_right: int
            Right border of the segment with root in current_index.

        action: Callable
            Operation to query among available for the tree.

        query_left: int
            Left border of the range, included in the query.

        query_right: int
            Right border of the range, included in the query.

        Returns
        -------
        float
            The result of the query.

        """

        if query_left <= segment_left and query_right >= segment_right:
            return self.tree[current_index] \
                if isinstance(self.tree[current_index], int) \
                else self.tree[current_index][self.action.index(action)]
        if query_right < segment_left or query_left > segment_right:
            if action in [gcd, sum]:
                return 0
            elif action == min:
                return float('inf')
            elif action == max:
                return -float('inf')
            else:
                return self.neutral[action]

        mid = (segment_left + segment_right) // 2
        left_index = 2 * current_index + 1
        right_index = 2 * current_index + 2

        left_query = self._query(
            left_index, segment_left, mid,
            action, query_left, query_right)
        right_query = self._query(
            right_index, mid + 1, segment_right,
            action, query_left, query_right)

        if action not in [min, max, gcd]:
            return action([left_query, right_query])
        else:  # action in [action. sum]
            return action(left_query, right_query)

    def update(self, index: int, new_value: float) -> None:
        """
        Updates the value of a specified index in the segment tree.

        Parameters
        ----------
        index: int
            Index to update.

        new_value: float
            New value to assign to the specified index.

        Returns
        -------
        None

        """

        self._update(0, 0, self.n - 1, index, new_value)

    def _update(self, current_index: int, segment_left: int,
                segment_right: int, index: int, new_value: float) -> None:
        """
        Recursively updates the value of a specified index in the
        segment tree.

        Parameters
        ----------
        current_index: int
            Index for which the function currently calculates actions.

        segment_left: int
            Left border of the segment with root in current_index.

        segment_right: int
            Right border of the segment with root in current_index.

        index: int
            Index to update.

        new_value: float
            New value to assign to the specified index.

        Returns
        -------
        None

        """

        if segment_left == segment_right == index:
            self.tree[current_index] = new_value
            return

        mid = (segment_left + segment_right) // 2
        left_index = 2 * current_index + 1
        right_index = 2 * current_index + 2

        if index <= mid:
            self._update(left_index, segment_left, mid, index, new_value)
        else:
            self._update(right_index, mid + 1, segment_right, index,
                         new_value)

        left_query, right_query = \
            self.determine_queries(left_index, right_index)

        self.tree[current_index] = \
            [func([left_query(i), right_query(i)])
             if func != gcd
             else func(*[left_query(i), right_query(i)])
             for i, func in enumerate(self.action)]

    def new_action(self, func: Callable, neutral: float) -> None:
        """
        Adds a new action to the segment tree and updates the tree
        accordingly.

        Parameters
        ----------
        func: Callable
            The new action to add to the segment tree.

        neutral
            The neutral element associated with the new action.

        Returns
        -------
        None

        """

        self.action.append(func)
        self.build_tree(self.arr, 0, 0, self.n - 1, func)
        self.neutral[func] = neutral
