import pytest

from Algorithms.python_solutions.edit_distance import edit_distance, \
    jaro_distance, hamming_distance


@pytest.mark.parametrize('str1, str2, output', [
    ('hello', 'holla', 0.73333333),
    ('cat', 'cat', 1.0),
    ('apple', 'banana', 0.45555555),
    # bounds
    ('', 'abc', 0),
    ('abc', '', 0),
    ('', '', 0),
    ('cattatat', 'actatata', 0.7738095),
    ('abc', 'def', 0)
])
def test_jaro_distance(str1, str2, output):
    assert abs(jaro_distance(str1, str2) - output) <= 10e-6


@pytest.mark.parametrize("input1, input2, output", [
    ("karolin", "kathrin", 3),
    ("karolina", "kathrine", 4),
    ("1011101", "1001001", 2)
])
def test_hamming_distance(input1, input2, output):
    assert hamming_distance(input1, input2) == output


def test_hamming_error():
    with pytest.raises(ValueError):
        hamming_distance('a', 'ab')


@pytest.mark.parametrize("input1, input2, method, expected", [
    ("hello", "holla", "jaro", 0.73333333),
    ("apple", "banana", "jaro", 0.45555555),
    ("karolin", "kathrin", "hamming", 3),
    ("karolina", "kathrine", "hamming", 4),
    ("kitten", "sitting", "dl", 3),
    ("flaw", "lawn", "dl", 2),
    ("kitten", "sitting", "lcs", 4),
    ("flaw", "lawn", "lcs", 3)
])
def test_edit_distance(input1, input2, method, expected):
    assert abs(edit_distance(
        input1, input2,
        distance=method) - expected) <= 10e-6
