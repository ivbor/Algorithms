import pytest

from Algorithms.python_solutions.sparse_table import SparseTable

sample_data = [3, 1, 4, 1, 5, 9, 2, 6]


@pytest.fixture
def sparse_table_instance():
    return SparseTable(sample_data)


def test_query_min(sparse_table_instance):
    assert sparse_table_instance.query_min(0, 3) == min(sample_data[0:4])
    assert sparse_table_instance.query_min(1, 5) == min(sample_data[1:6])
    assert sparse_table_instance.query_min(2, 7) == min(sample_data[2:8])


def test_query_max(sparse_table_instance):
    assert sparse_table_instance.query_max(0, 3) == max(sample_data[0:4])
    assert sparse_table_instance.query_max(1, 5) == max(sample_data[1:6])
    assert sparse_table_instance.query_max(2, 7) == max(sample_data[2:8])


def test_query_sum(sparse_table_instance):
    assert sparse_table_instance.query_sum(0, 3) == sum(sample_data[0:4])
    assert sparse_table_instance.query_sum(1, 5) == sum(sample_data[1:6])
    assert sparse_table_instance.query_sum(2, 7) == sum(sample_data[2:8])


def test_append_and_extend_raise_errors(sparse_table_instance):
    with pytest.raises(TypeError):
        sparse_table_instance.append(10)
    with pytest.raises(TypeError):
        sparse_table_instance.extend([10, 20])
