# tests and docs
from math import gcd
from typing import Callable


class SegmentTree(list):
    def __init__(self, arr):
        super().__init__(arr)
        self.n = len(arr)
        self.tree_size = 2 ** (self.n - 1).bit_length() << 1
        self.tree_sum = [0] * self.tree_size
        self.tree_min = [float('inf')] * self.tree_size
        self.tree_max = [-float('inf')] * self.tree_size
        self.tree_gcd = [0] * self.tree_size

        # Build the segment tree using recursive function
        self.build_tree(0, 0, self.n - 1)

    def build_tree(self, current_index, left, right):
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

    def query(self, action, query_left, query_right):
        return self._query(0, 0, self.n - 1, action, query_left, query_right)

    def _query(self, current_index, segment_left, segment_right, action,
               query_left, query_right):
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
        elif action == min:
            return min(left_query, right_query)
        elif action == max:
            return max(left_query, right_query)
        elif action == gcd:
            return gcd(left_query, right_query)

    def update(self, index, new_value):
        self._update(0, 0, self.n - 1, index, new_value)

    def _update(self, current_index, segment_left,
                segment_right, index, new_value):
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

    def __init__(self, arr):
        self.n = len(arr)
        self.tree_size = 2 ** (self.n - 1).bit_length() << 1
        self.tree = [None] * (self.tree_size)
        self.action = [sum, min, max, gcd]
        self.build_tree(arr, 0, 0, self.n - 1)
        self.arr = arr
        self.neutral = dict()

    # function reducing memory consumption from 8n to (5n - 4)
    def determine_queries(self, left_index, right_index):

        if isinstance(self.tree[left_index], list) and \
           isinstance(self.tree[right_index], list):
            left_query = \
                lambda x: self.tree[left_index][x]
            right_query = \
                lambda x: self.tree[right_index][x]
        elif isinstance(self.tree[left_index], list) and \
                isinstance(self.tree[right_index], int):
            left_query = \
                lambda x: self.tree[left_index][x]
            right_query = \
                lambda x: self.tree[right_index]
        elif isinstance(self.tree[left_index], int) and \
                isinstance(self.tree[right_index], int):
            left_query = \
                lambda x: self.tree[left_index]
            right_query = \
                lambda x: self.tree[right_index]

        return left_query, right_query

    def build_tree(self, arr, current_index, left, right, action=None):
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

    def query(self, action, query_left, query_right):
        return self._query(0, 0, self.n - 1, action, query_left, query_right)

    def _query(self, current_index, segment_left,
               segment_right, action, query_left, query_right):
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

        if action == sum:
            return sum([left_query, right_query])
        elif action == min:
            return min(left_query, right_query)
        elif action == max:
            return max(left_query, right_query)
        elif action == gcd:
            return gcd(left_query, right_query)
        else:
            return action([left_query, right_query])

    def update(self, index, new_value):
        self._update(0, 0, self.n - 1, index, new_value)

    def _update(self, current_index, segment_left,
                segment_right, index, new_value):
        if segment_left == segment_right == index:
            self.tree[current_index] = new_value
            return

        mid = (segment_left + segment_right) // 2
        left_index = 2 * current_index + 1
        right_index = 2 * current_index + 2

        if index <= mid:
            self._update(left_index, segment_left, mid, index, new_value)
        else:
            self._update(right_index, mid + 1, segment_right, index, new_value)

        left_query, right_query = \
            self.determine_queries(left_index, right_index)

        self.tree[current_index] = \
            [func([left_query(i), right_query(i)])
             if func != gcd
             else func(*[left_query(i), right_query(i)])
             for i, func in enumerate(self.action)]

    def new_action(self, func: Callable, neutral):
        self.action.append(func)
        self.build_tree(self.arr, 0, 0, self.n - 1, func)
        self.neutral[func] = neutral
