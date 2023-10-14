# TODO
# write tests for the function with (generated) test cases
# write time and space complexities for all functions
# (maybe) write naive solutions' time and space complexities
# write some additional problems including but not limited to:
#   matrix chain multiplication (with and without chain order multiplication
#   and time and space complexities for them)
#   travelling salesman (bitmask dynamic programming etc.)
#   longest increasing subsequence (with and without binary search)
#   optimal binary search tree
#   coin change

class DynamicProgrammingProblem:
    def __init__(self):
        self.dp = None

    def solve(self):
        raise NotImplementedError("Subclasses must implement the solve method")


class KnapsackProblem(DynamicProgrammingProblem):
    def __init__(self, weights, values, capacity):
        super().__init__()
        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.num_items = len(weights)

    def solve(self):
        # dynamic programming table for this problem includes
        # amount of rows equal to the amount of items and
        # amount of columns equal to the capacity
        # for capacity == 0 there are no items we can place
        self.dp = [[0] * (self.capacity + 1)
                   for _ in range(self.num_items + 1)]

        # start to fill the table
        for i in range(1, self.num_items + 1):
            for w in range(1, self.capacity + 1):
                # check if weight of i-1 item can fit inside
                # current capacity which is w
                if self.weights[i - 1] <= w:
                    self.dp[i][w] = max(
                        self.dp[i - 1][w],
                        self.dp[i - 1][w - self.weights[i - 1]] +
                        self.values[i - 1])
                else:
                    self.dp[i][w] = self.dp[i - 1][w]
        return self.dp[self.num_items][self.capacity]


class LongestCommonSubsequence(DynamicProgrammingProblem):
    def __init__(self, str1, str2):
        super().__init__()
        self.str1 = str1
        self.str2 = str2
        self.m = len(str1)
        self.n = len(str2)

    def solve(self):
        self.dp = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                if self.str1[i - 1] == self.str2[j - 1]:
                    self.dp[i][j] = self.dp[i - 1][j - 1] + 1
                else:
                    self.dp[i][j] = max(self.dp[i - 1][j], self.dp[i][j - 1])
        return self.dp[self.m][self.n]


class DamerauLevensteinDistance(DynamicProgrammingProblem):
    def __init__(self, str1, str2):
        super().__init__()
        self.str1 = str1
        self.str2 = str2
        self.m = len(str1)
        self.n = len(str2)

    def solve(self):
        self.dp = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        for i in range(self.m + 1):
            self.dp[i][0] = i
        for j in range(self.n + 1):
            self.dp[0][j] = j

        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                cost = 0 \
                    if self.str1[i - 1] == self.str2[j - 1] else 1
                self.dp[i][j] = min(
                    self.dp[i - 1][j] + 1,  # Deletion
                    self.dp[i][j - 1] + 1,  # Insertion
                    self.dp[i - 1][j - 1] + cost  # Substitution
                )
                if 1 < i and i < self.m and 1 < j and j < self.n:
                    if (self.str1[i] == self.str2[j - 1]) \
                            and (self.str1[i - 1] == self.str2[j]):
                        self.dp[i][j] = min(
                            self.dp[i][j],
                            self.dp[i - 2][j - 2] + 1)  # Transposition
        return self.dp[self.m][self.n]


class LevensteinDistanceOptimized(DynamicProgrammingProblem):
    def __init__(self, str1, str2):
        super().__init__()
        self.str1 = str1
        self.str2 = str2

    def solve(self):
        m, n = len(self.str1), len(self.str2)

        # Ensure str1 is the shorter string
        if m > n:
            self.str1, self.str2, m, n = self.str2, self.str1, n, m

        # Initialize a 1D array to store the current and previous row
        self.dp = [0] * (m + 1)

        # Initialize the first row
        for i in range(m + 1):
            self.dp[i] = i

        for j in range(1, n + 1):
            prev_diag = self.dp[0]  # Store the previous diagonal value
            self.dp[0] = j  # Update the first element in the current row

            for i in range(1, m + 1):
                insert_cost = self.dp[i - 1] + 1
                delete_cost = self.dp[i] + 1
                replace_cost = prev_diag + \
                    (0 if self.str1[i - 1] == self.str2[j - 1] else 1)
                prev_diag, self.dp[i] = \
                    self.dp[i], min(insert_cost, delete_cost, replace_cost)

        return self.dp[m]
