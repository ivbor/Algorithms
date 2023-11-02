# TODO
# tests and docs
import math


class SparseTable(tuple):
    def __init__(self, arr):
        super().__init__()
        self.N = len(arr)
        # Number of bits needed to represent N
        self.K = int(math.log2(self.N) + 1)
        self.table_min = [[0] * self.K for _ in range(self.N)]
        self.table_max = [[0] * self.K for _ in range(self.N)]
        self.table_sum = [[0] * self.K for _ in range(self.N)]

        for i in range(self.N):
            self.table_min[i][0] = arr[i]
            self.table_max[i][0] = arr[i]
            self.table_sum[i][0] = arr[i]

        for j in range(1, self.K):
            for i in range(self.N - (1 << j) + 1):
                self.table_min[i][j] = min(
                    self.table_min[i][j - 1],
                    self.table_min[i + (1 << (j - 1))][j - 1])
                self.table_max[i][j] = max(
                    self.table_max[i][j - 1],
                    self.table_max[i + (1 << (j - 1))][j - 1])
                self.table_sum[i][j] = self.table_sum[i][j - 1] + \
                    self.table_sum[i + (1 << (j - 1))][j - 1]

    def __new__(cls, arr):
        return super(SparseTable, cls).__new__(cls, tuple(arr))

    def append(self, x):
        raise TypeError('SparseTable cannot be changed after creation')

    def extend(self, x):
        raise TypeError('SparseTable cannot be changed after creation')

    def query_min(self, left, right):
        k = int(math.log2(right - left + 1))
        return min(
            self.table_min[left][k],
            self.table_min[right - (1 << k) + 1][k])

    def query_max(self, left, right):
        k = int(math.log2(right - left + 1))
        return max(
            self.table_max[left][k],
            self.table_max[right - (1 << k) + 1][k])

    def query_sum(self, left, right):
        total_sum = 0
        k = int(math.log2(right - left + 1))
        for j in range(k, -1, -1):
            if (1 << j) <= (right - left + 1):
                total_sum += self.table_sum[left][j]
                left += 1 << j

        return total_sum
