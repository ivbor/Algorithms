# TODO
# write tests for the function with (generated) test cases
# (maybe) find, adapt or generate hard test cases
# write time and space complexities for all functions
# (maybe) write naive solutions and their time and space complexities
# write some additional problems (with modifying basic dp function
# with decorator) including but not limited to:
#   matrix chain multiplication (with and without chain order multiplication
#   and time and space complexities for them)
#   levenshtein distance (with and without calculating values row by row and
#   time and space complexities for them)
#   travelling salesman (bitmask dynamic programming etc.)
#   longest increasing subsequence
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
        self.dp = [[0] * (self.capacity + 1)
                   for _ in range(self.num_items + 1)]
        for i in range(1, self.num_items + 1):
            for w in range(1, self.capacity + 1):
                if self.weights[i - 1] <= w:
                    self.dp[i][w] = max(
                        self.dp[i - 1][w],
                        self.dp[i - 1][w - self.weights[i - 1]] + self.values
                        [i - 1])
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


class LevenshteinDistance(DynamicProgrammingProblem):
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
                cost = 0 if self.str1[i - 1] == self.str2[j - 1] else 1
                self.dp[i][j] = min(
                    self.dp[i - 1][j] + 1,  # Deletion
                    self.dp[i][j - 1] + 1,  # Insertion
                    self.dp[i - 1][j - 1] + cost  # Substitution
                )
        return self.dp[self.m][self.n]
