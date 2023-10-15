# TODO
# docs
# travelling salesman (bitmask dynamic programming etc.)
import logging


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
                if (self.str1[i - 1] == self.str2[j - 2]) \
                        and (self.str1[i - 2] == self.str2[j - 1]):
                    self.dp[i][j] = min(
                        self.dp[i][j],
                        self.dp[i - 2][j - 2] + 1)  # Transposition
        logging.debug(self.dp)
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
        self.dp = [[0] * (m + 1) for _ in range(3)]

        # Initialize the first row
        for i in range(m + 1):
            self.dp[0][i] = i

        current_row = 0
        for j in range(1, n + 1):
            logging.debug(' j = ' + f'{j}')
            # Store the previous row
            logging.debug('current_row = ' + f'{current_row}')
            current_row = 1 + current_row if current_row < 2 else 0

            logging.debug('current_row = ' + f'{current_row}')

            # Update the first element in the current row
            self.dp[current_row][0] = j

            for i in range(1, m + 1):
                logging.debug(' i = ' + f'{i}')
                cost = \
                    0 if self.str1[i - 1] == self.str2[j - 1] else 1

                insert_cost = self.dp[current_row][i - 1] + 1
                delete_cost = self.dp[current_row - 1][i] + 1
                replace_cost = self.dp[current_row - 1][i - 1] + cost
                transposition_cost = self.dp[current_row - 2][i - 2] + 1
                logging.debug(f''' costs: {insert_cost}, {delete_cost}, ''' +
                              f'''{replace_cost}, ''' +
                              f'''{transposition_cost}''')

                logging.debug(f'{self.dp}')
                self.dp[current_row][i] = \
                    min(insert_cost, delete_cost, replace_cost)
                logging.debug(f'{self.dp}')
                if (self.str1[j - 1] == self.str2[i - 2] and
                        self.str1[j - 2] == self.str2[i - 1]):
                    self.dp[current_row][i] = \
                        min(self.dp[current_row][i],
                            self.dp[current_row - 2][i - 2] + 1)
                logging.debug(f'{self.dp}')

        return self.dp[current_row][m]


class LongestIncreasingSubsequence(DynamicProgrammingProblem):

    def __init__(self, nums):
        super().__init__()
        self.nums = nums

    def solve(self):
        if not self.nums:
            return 0

        n = len(self.nums)
        # Initialize the LIS array with a length of 1 for each element
        self.dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if self.nums[i] > self.nums[j]:
                    self.dp[i] = max(self.dp[i], self.dp[j] + 1)

        return max(self.dp)


class LongestIncreasingSubsequenceOptimized(DynamicProgrammingProblem):
    '''This implementation uses binary search'''

    def __init__(self, nums):
        super().__init__()
        self.nums = nums

    def solve(self):
        if not self.nums:
            return 0

        n = len(self.nums)
        # using dp for representing the smallest tail of all
        # increasing subsequences of length i
        self.dp = [0] * n
        self.dp[0] = self.nums[0]

        # Initialize the length of the LIS to 1
        length = 1

        for i in range(1, n):
            if self.nums[i] < self.dp[0]:
                self.dp[0] = self.nums[i]
            elif self.nums[i] > self.dp[length - 1]:
                self.dp[length] = self.nums[i]
                length += 1
            else:
                # Find the position of the smallest element in tails
                # that is greater than or equal to nums[i]
                left, right = 0, length - 1
                while left < right:
                    mid = (left + right) // 2
                    if self.dp[mid] < self.nums[i]:
                        left = mid + 1
                    else:
                        right = mid
                self.dp[left] = self.nums[i]
        return length
