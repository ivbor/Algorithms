import pytest
import subprocess
import random

from ctypes import c_int, POINTER, CDLL

from Algorithms.python_solutions.dynamic_programming \
    import KnapsackProblem, LevenshteinDistance, LongestCommonSubsequence


def generate_test_cases_with_output_for_knapsack():
    ''' some test cases generation and automatic solving'''

    # generate text file with problem's conditions
    n = random.randint(5, 100)
    r = random.randint(10, 1000)
    t = random.randint(1, 16)
    i = random.randint(0, 200)
    S = random.randint(100, 2000)
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


@pytest.mark.parametrize("test_input, test_output",
                         generate_test_cases(
                             generate_test_cases_with_output_for_knapsack,
                             20))
def test_knapsack_problem(test_input, test_output):
    # test_input = (weights, values, capacity)
    assert KnapsackProblem(*test_input).solve() == test_output
