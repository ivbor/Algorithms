import pytest
import subprocess
import random
import string

from ctypes import c_int, POINTER, CDLL, c_char

from Algorithms.python_solutions.dynamic_programming \
    import KnapsackProblem, DamerauLevensteinDistance, \
    LongestCommonSubsequence, DynamicProgrammingProblem, \
    LevensteinDistanceOptimized


def test_dp_class_solve_raises():
    with pytest.raises(Exception):
        DynamicProgrammingProblem.solve()


def generate_test_cases_with_output_for_knapsack(
    n_start=5, n_end=100, r_start=10, r_end=1000, t_start=1, t_end=16,
    i_start=0, i_end=200, S_start=100, S_end=2000
):
    ''' some test cases generation and automatic solving'''

    # generate text file with problem's conditions
    n = random.randint(n_start, n_end)
    r = random.randint(r_start, r_end)
    t = random.randint(t_start, t_end)
    i = random.randint(i_start, i_end)
    S = random.randint(S_start, S_end)
    subprocess.run(['./Algorithms/C_solutions/genhard', f'{n}',
                    f'{r}', f'{t}', '{i}', f'{S}'])

    # read generated text file
    test_values = []
    file = open('./Algorithms/C_solutions/test.in')
    line = '1'  # non-empty line so that while would start
    while line != '':
        line = file.readline().split('\n')[0]
        test_values.append(line)

    # parsing data from generated file to put it inside solver
    capacity = int(test_values[-2])
    n_items = int(test_values[0])
    test_values = test_values[1:-2]
    values = list()
    weights = list()
    for i in test_values:
        values.append(int(i[5:11].replace(' ', '')))
        weights.append(int(i[11:].replace(' ', '')))
    solutions = [0 for _ in test_values]

    # initialize c interface and convert parsed data to the appropriate c_types
    c_lib = CDLL('./Algorithms/C_solutions/minknap.so')
    c_lib.minknap.argtypes = [c_int, POINTER(c_int), POINTER(c_int),
                              POINTER(c_int), c_int]
    seq = c_int * len(test_values)
    c_values = seq(*values)
    c_weights = seq(*weights)
    c_solutions = seq(*solutions)

    # solve the problem
    res = c_lib.minknap(n_items, c_values, c_weights,
                        c_solutions, capacity)

    # return test conditions in the format for convenient parametrization
    return ((weights, values, capacity), res)


def generate_test_cases(function, amount=20):
    res = list()
    for _ in range(amount):
        res.append(function())
    return res


@ pytest.mark.parametrize("test_input, test_output",
                          generate_test_cases(
                             generate_test_cases_with_output_for_knapsack,
                             20))
def test_knapsack_problem(test_input, test_output):
    # test_input = (weights, values, capacity)
    assert KnapsackProblem(*test_input).solve() == test_output


def test_knapsack_bounds():
    assert KnapsackProblem([], [], 0).solve() == 0
    assert KnapsackProblem([12], [1], 0).solve() == 0
    assert KnapsackProblem([15, 1, 12], [10000, 1, 0], 14).solve() == 1


def test_damerau_levenstein_bounds():
    assert DamerauLevensteinDistance('', '').solve() == 0
    char1 = random.SystemRandom().choice(
        string.ascii_uppercase + string.digits)
    char2 = random.SystemRandom().choice(
        string.ascii_uppercase + string.digits)
    assert DamerauLevensteinDistance(char1, char2).solve() == 1
    str1 = ''.join(random.SystemRandom().choice(
        string.ascii_uppercase + string.digits) for _ in range(10))
    assert DamerauLevensteinDistance(str1, '').solve() == len(str1)


def generate_test_cases_with_output_for_damerau_levenstein(
        str1_len=10, str2_len=10):

    str1 = ''.join(random.SystemRandom().choice(
        string.ascii_uppercase + string.digits) for _ in range(str1_len))
    str2 = ''.join(random.SystemRandom().choice(
        string.ascii_uppercase + string.digits) for _ in range(str2_len))

    # initialize c interface and convert parsed data
    # to the appropriate c_types
    c_lib = CDLL('./Algorithms/C_solutions/damerau_levenstein.so')
    c_lib.DamerauLevensteinDistance.argtypes = \
        [POINTER(c_char), POINTER(c_char)]
    seq_str1 = c_char * len(str1)
    seq_str2 = c_char * len(str2)
    c_str1 = seq_str1(*str1.encode())
    c_str2 = seq_str2(*str2.encode())

    # solve the problem
    res = c_lib.DamerauLevensteinDistance(c_str1, c_str2)

    return ((str1, str2), res)


@ pytest.mark.parametrize(
    "test_input, test_output",
    generate_test_cases(
                    generate_test_cases_with_output_for_damerau_levenstein,
                    20))
def test_damerau_levenstein(test_input, test_output):
    # test_input = (str1, str2)
    assert DamerauLevensteinDistance(*test_input).solve() == test_output
    assert LevensteinDistanceOptimized(*test_input).solve() == test_output


def test_lcs_bounds():
    assert LongestCommonSubsequence('', '').solve() == 0
    assert LongestCommonSubsequence('abc', '').solve() == 0
    assert LongestCommonSubsequence('', 'abc').solve() == \
        LongestCommonSubsequence('abc', '').solve()
    assert LongestCommonSubsequence('abc', 'abc').solve() == 3


# test cases are from here:
# https://workat.tech/problem-solving/practice/longest-common-subsequence
@ pytest.mark.parametrize('test_input, test_output',
                          [(('workattech', 'branch'), 4),
                           (('helloworld', 'playword'), 5),
                           (('hello', 'hello'), 5),
                           (('abc', 'def'), 0)])
def test_some_lcs_test_cases(test_input, test_output):
    assert LongestCommonSubsequence(*test_input).solve() == test_output
