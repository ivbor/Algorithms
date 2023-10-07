# TODO
# write tests for the function with (generated) test cases
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


def dynamic_programming(problem_params, transition_function, dimensions=2):
    """
    Solve a dynamic programming problem using the given transition function.

    Parameters
    ----------
    problem_params: tuple or list
        Contains problem-specific parameters to be passed to the
        transition_function.

    transition_function: callable
        A function that calculates the transition values using problem_params.

    dimensions: int
        A number of dimensions inside dynamic programming table required
        for solving a particular problem. Default is 2.

    Returns
    -------
    any
        The solution to the dynamic programming problem.

    """
    n = len(problem_params[0])

    # Create a table for memorization
    # Fill in the table using the transition function
    # Return the final result (specific to the problem)
    if dimensions == 1:
        dp = [0] * n

        for i in range(1, n):
            dp[i] = transition_function(dp, i, problem_params)

        return dp[n]

    elif dimensions == 2:
        dp = [[0] * n for _ in range(n)]

        for i in range(1, n):
            for j in range(1, n):
                dp[i][j] = transition_function(dp, i, j, problem_params)

        return dp[n][n]

    elif dimensions == 3:
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]

        for i in range(1, n):
            for j in range(1, n):
                for k in range(1, n):
                    dp[i][j][k] = transition_function(dp, i, j, k,
                                                      problem_params)
        return dp[n][n][n]

    else:
        raise NotImplementedError('problems with tables having more' +
                                  ' than 3 dimensions are not supported')


# Example 1: Knapsack problem

# With the use of dynamic programming time complexity is O(n*W)
# instead of O(2^n) on low W
def knapsack_transition(dp, i, j, params):
    weight, value = params
    if weight[i - 1] <= j:
        return max(dp[i - 1][j], dp[i - 1][j - weight[i - 1]] + value[i - 1])
    else:
        return dp[i - 1][j]


weights = [2, 1, 3, 2]
values = [3, 2, 4, 2]
problem_params = (weights, values)

knapsack_solution = dynamic_programming(
    problem_params, knapsack_transition)
print("Knapsack Problem Solution:", knapsack_solution)


# Example 2: Longest Common Subsequence (LCS) problem
def lcs_transition(dp, i, j, params):
    str1, str2 = params
    if str1[i - 1] == str2[j - 1]:
        return dp[i - 1][j - 1] + 1
    else:
        return max(dp[i - 1][j], dp[i][j - 1])


str1 = "AGGTAB"
str2 = "GXTXAYB"
problem_params = (str1, str2)

lcs_length = dynamic_programming(problem_params, lcs_transition)
print("Longest Common Subsequence Length:", lcs_length)
