# ternary_search_module

This module provides two functions, `tern_search_min` and `tern_search_max`,
for finding the minimum and maximum values of a function within a specified
range, respectively. These search algorithms are suitable for cases where
the function has only one minimum or maximum value within the given range.

Functions
---------
tern_search_min(func, start, end, eps=1e-6)
    Find the minimum value of a function within a specified range.

tern_search_max(func, start, end, eps=1e-6)
    Find the maximum value of a function within a specified range.

<a id="python_solutions.ternary_search_extremum.tern_search_min"></a>

#### tern\_search\_min

```python
def tern_search_min(func, start, end, eps=1e-6)
```

Ternary search for finding the minimum value of a function
within a specified range.

This search algorithm is suitable for cases where the function has
only one minimum value within the given range [start, end].
This ternary search algorithm works with a time complexity of O(log2(n)),
where n is the number of times the epsilon (eps) can fit in the absolute
difference between the start and end positions.
It determines the local minimum by comparing the function's values
at two points within the search interval.

## Parameters
- **func**: callable

    The function for which to find the minimum value.

- **start**: float

    The start of the range for the search.

- **end**: float

    The end of the range for the search.

- **eps**: float, optional

    The epsilon parameter controlling the accuracy
    of search. Default is 1e-6.

## Returns

float
    The approximate x-coordinate of the minimum value of the function
    within the specified range.

<a id="python_solutions.ternary_search_extremum.tern_search_max"></a>

#### tern\_search\_max

```python
def tern_search_max(func, start, end, eps=1e-6)
```

Ternary search for finding the maximum value of a function
within a specified range.

This search algorithm is suitable for cases where the function has
only one maximum value within the given range [start, end].
This ternary search algorithm works with a time complexity of O(log2(n)),
where n is the number of times the epsilon (eps) can fit in the absolute
difference between the start and end positions.
It determines the local minimum by comparing the function's values
at two points within the search interval.

## Parameters
- **func**: callable

    The function for which to find the maximum value.

- **start**: float

    The start of the range for the search.

- **end**: float

    The end of the range for the search.

- **eps**: float, optional

    The epsilon parameter controlling the accuracy of the search.
    Default is 1e-6.

## Returns

float
    The approximate x-coordinate of the maximum value of the function
    within the specified range.

<a id="python_solutions.tests.test_array_count_sort.random"></a>

## random

<a id="python_solutions.tests.test_array_count_sort.array_count_sort"></a>

## array\_count\_sort

<a id="python_solutions.tests.test_array_count_sort.test_array_count_sort_case_one_elt_with_huge_variation"></a>

#### test\_array\_count\_sort\_case\_one\_elt\_with\_huge\_variation

```python
def test_array_count_sort_case_one_elt_with_huge_variation()
```

<a id="python_solutions.tests.test_array_count_sort.test_array_count_sort_case_one_elt_in_2_dim"></a>

#### test\_array\_count\_sort\_case\_one\_elt\_in\_2\_dim

```python
def test_array_count_sort_case_one_elt_in_2_dim()
```

<a id="python_solutions.tests.test_array_count_sort.test_array_count_sort_case_one_elt_in_2_dim_some_empty"></a>

#### test\_array\_count\_sort\_case\_one\_elt\_in\_2\_dim\_some\_empty

```python
def test_array_count_sort_case_one_elt_in_2_dim_some_empty()
```

<a id="python_solutions.tests.test_array_count_sort.test_array_count_sort_case_many_elts_no_key"></a>

#### test\_array\_count\_sort\_case\_many\_elts\_no\_key

```python
def test_array_count_sort_case_many_elts_no_key()
```

<a id="python_solutions.tests.test_array_count_sort.test_array_count_sort_case_many_elts_no_key_some_empty"></a>

#### test\_array\_count\_sort\_case\_many\_elts\_no\_key\_some\_empty

```python
def test_array_count_sort_case_many_elts_no_key_some_empty()
```

<a id="python_solutions.tests.test_array_count_sort.test_array_count_sort_case_many_elts_with_key_some_empty"></a>

#### test\_array\_count\_sort\_case\_many\_elts\_with\_key\_some\_empty

```python
def test_array_count_sort_case_many_elts_with_key_some_empty()
```

<a id="python_solutions.tests.test_avl_tree.pytest"></a>

## pytest

<a id="python_solutions.tests.test_avl_tree.random"></a>

## random

<a id="python_solutions.tests.test_avl_tree.math"></a>

## math

<a id="python_solutions.tests.test_avl_tree.AVLTree"></a>

## AVLTree

<a id="python_solutions.tests.test_avl_tree.avl_tree"></a>

#### avl\_tree

```python
@pytest.fixture
def avl_tree()
```

<a id="python_solutions.tests.test_avl_tree.test_insert"></a>

#### test\_insert

```python
def test_insert(avl_tree)
```

<a id="python_solutions.tests.test_avl_tree.test_delete"></a>

#### test\_delete

```python
def test_delete(avl_tree)
```

<a id="python_solutions.tests.test_avl_tree.test_delete_with_error"></a>

#### test\_delete\_with\_error

```python
def test_delete_with_error(avl_tree)
```

<a id="python_solutions.tests.test_avl_tree.test_search"></a>

#### test\_search

```python
def test_search(avl_tree)
```

<a id="python_solutions.tests.test_avl_tree.test_random_length_and_elts"></a>

#### test\_random\_length\_and\_elts

```python
def test_random_length_and_elts()
```

<a id="python_solutions.tests.test_bin_search.random"></a>

## random

<a id="python_solutions.tests.test_bin_search.bin_search"></a>

## bin\_search

<a id="python_solutions.tests.test_bin_search.test_bin_search_no_rec"></a>

#### test\_bin\_search\_no\_rec

```python
def test_bin_search_no_rec()
```

<a id="python_solutions.tests.test_bin_search.test_bin_search_with_rec"></a>

#### test\_bin\_search\_with\_rec

```python
def test_bin_search_with_rec()
```

<a id="python_solutions.tests.test_bloom_filter.pytest"></a>

## pytest

<a id="python_solutions.tests.test_bloom_filter.Bloom_filter"></a>

## Bloom\_filter

<a id="python_solutions.tests.test_bloom_filter.test_can_create_bloom_filter"></a>

#### test\_can\_create\_bloom\_filter

```python
def test_can_create_bloom_filter()
```

<a id="python_solutions.tests.test_bloom_filter.bf"></a>

#### bf

```python
@pytest.fixture
def bf()
```

<a id="python_solutions.tests.test_bloom_filter.test_can_add_to_bloom_filter"></a>

#### test\_can\_add\_to\_bloom\_filter

```python
def test_can_add_to_bloom_filter(bf)
```

<a id="python_solutions.tests.test_bloom_filter.test_can_create_bloom_filter_jenkins"></a>

#### test\_can\_create\_bloom\_filter\_jenkins

```python
def test_can_create_bloom_filter_jenkins()
```

<a id="python_solutions.tests.test_bloom_filter.test_false_positives_less_than_5_percent"></a>

#### test\_false\_positives\_less\_than\_5\_percent

```python
def test_false_positives_less_than_5_percent(bf)
```

<a id="python_solutions.tests.test_bloom_filter.test_bloom_filter_stress"></a>

#### test\_bloom\_filter\_stress

```python
def test_bloom_filter_stress()
```

<a id="python_solutions.tests.test_bloom_filter.test_long_strings_for_advanced_jenkins"></a>

#### test\_long\_strings\_for\_advanced\_jenkins

```python
def test_long_strings_for_advanced_jenkins()
```

<a id="python_solutions.tests.test_bloom_filter.test_raises_error_when_unrecognized_hash_passed"></a>

#### test\_raises\_error\_when\_unrecognized\_hash\_passed

```python
def test_raises_error_when_unrecognized_hash_passed()
```

<a id="python_solutions.tests.test_bst.pytest"></a>

## pytest

<a id="python_solutions.tests.test_bst.random"></a>

## random

<a id="python_solutions.tests.test_bst.BinarySearchTree"></a>

## BinarySearchTree

<a id="python_solutions.tests.test_bst.test_search_none"></a>

#### test\_search\_none

```python
def test_search_none()
```

<a id="python_solutions.tests.test_bst.test_insert_and_search_and_height"></a>

#### test\_insert\_and\_search\_and\_height

```python
def test_insert_and_search_and_height()
```

<a id="python_solutions.tests.test_bst.bst"></a>

#### bst

```python
@pytest.fixture
def bst()
```

<a id="python_solutions.tests.test_bst.test_in_order_traversal"></a>

#### test\_in\_order\_traversal

```python
def test_in_order_traversal(bst)
```

<a id="python_solutions.tests.test_bst.test_successor_predecessor"></a>

#### test\_successor\_predecessor

```python
def test_successor_predecessor(bst)
```

<a id="python_solutions.tests.test_bst.test_delete"></a>

#### test\_delete

```python
def test_delete(bst)
```

<a id="python_solutions.tests.test_bst.test_delete_with_error"></a>

#### test\_delete\_with\_error

```python
def test_delete_with_error(bst)
```

<a id="python_solutions.tests.test_bst.test_search"></a>

#### test\_search

```python
def test_search(bst)
```

<a id="python_solutions.tests.test_bst.test_height_advanced"></a>

#### test\_height\_advanced

```python
def test_height_advanced(bst)
```

<a id="python_solutions.tests.test_bst.test_find_min_and_max"></a>

#### test\_find\_min\_and\_max

```python
def test_find_min_and_max()
```

<a id="python_solutions.tests.test_bst.test_random_length_and_elts"></a>

#### test\_random\_length\_and\_elts

```python
def test_random_length_and_elts()
```

<a id="python_solutions.tests.test_bst.test_local_tree"></a>

#### test\_local\_tree

```python
def test_local_tree(bst)
```

<a id="python_solutions.tests.test_CyclicLinkedList.CyclicLinkedList"></a>

## CyclicLinkedList

<a id="python_solutions.tests.test_CyclicLinkedList.DoubleNode"></a>

## DoubleNode

<a id="python_solutions.tests.test_CyclicLinkedList.pytest"></a>

## pytest

<a id="python_solutions.tests.test_CyclicLinkedList.test_can_make_cll"></a>

#### test\_can\_make\_cll

```python
def test_can_make_cll()
```

<a id="python_solutions.tests.test_CyclicLinkedList.cll"></a>

#### cll

```python
@pytest.fixture()
def cll()
```

<a id="python_solutions.tests.test_CyclicLinkedList.head"></a>

#### head

```python
@pytest.fixture()
def head()
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_can_initialize_cll_given_head"></a>

#### test\_can\_initialize\_cll\_given\_head

```python
def test_can_initialize_cll_given_head(head)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_initialize_from_chain"></a>

#### test\_initialize\_from\_chain

```python
def test_initialize_from_chain(head)
```

<a id="python_solutions.tests.test_CyclicLinkedList.cll_with_node"></a>

#### cll\_with\_node

```python
@pytest.fixture()
def cll_with_node(cll, head)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_insert_in_cll"></a>

#### test\_insert\_in\_cll

```python
def test_insert_in_cll(cll)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_insert_in_the_head"></a>

#### test\_insert\_in\_the\_head

```python
def test_insert_in_the_head(cll_with_node)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_raises_when_inserting_futher_than_append_goes"></a>

#### test\_raises\_when\_inserting\_futher\_than\_append\_goes

```python
def test_raises_when_inserting_futher_than_append_goes(cll_with_node)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_update_in_cll"></a>

#### test\_update\_in\_cll

```python
def test_update_in_cll(cll_with_node)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_erase_in_cll"></a>

#### test\_erase\_in\_cll

```python
def test_erase_in_cll(cll_with_node)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_erase_by_index_not_existing"></a>

#### test\_erase\_by\_index\_not\_existing

```python
def test_erase_by_index_not_existing(cll_with_node)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_erase_head"></a>

#### test\_erase\_head

```python
def test_erase_head(cll_with_node)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_erase_by_neg_index"></a>

#### test\_erase\_by\_neg\_index

```python
def test_erase_by_neg_index(cll_with_node)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_erase_tail"></a>

#### test\_erase\_tail

```python
def test_erase_tail(cll_with_node)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_raises_when_nothing_to_erase"></a>

#### test\_raises\_when\_nothing\_to\_erase

```python
def test_raises_when_nothing_to_erase(cll)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_insert_for_many_elements"></a>

#### test\_insert\_for\_many\_elements

```python
def test_insert_for_many_elements(cll)
```

<a id="python_solutions.tests.test_CyclicLinkedList.cll_with_many_nodes"></a>

#### cll\_with\_many\_nodes

```python
@pytest.fixture()
def cll_with_many_nodes(cll)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_can_update_many_elements"></a>

#### test\_can\_update\_many\_elements

```python
def test_can_update_many_elements(cll_with_many_nodes)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_erase_works_for_many_elements"></a>

#### test\_erase\_works\_for\_many\_elements

```python
def test_erase_works_for_many_elements(cll_with_many_nodes)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_insert_using_neg_index"></a>

#### test\_insert\_using\_neg\_index

```python
def test_insert_using_neg_index(cll_with_many_nodes)
```

<a id="python_solutions.tests.test_Deque.Deque"></a>

## Deque

<a id="python_solutions.tests.test_Deque.pytest"></a>

## pytest

<a id="python_solutions.tests.test_Deque.test_can_make_deck"></a>

#### test\_can\_make\_deck

```python
def test_can_make_deck()
```

<a id="python_solutions.tests.test_Deque.d"></a>

#### d

```python
@pytest.fixture()
def d()
```

<a id="python_solutions.tests.test_Deque.test_push_front_works_for_deque"></a>

#### test\_push\_front\_works\_for\_deque

```python
def test_push_front_works_for_deque(d)
```

<a id="python_solutions.tests.test_Deque.test_push_back_works_for_deque"></a>

#### test\_push\_back\_works\_for\_deque

```python
def test_push_back_works_for_deque(d)
```

<a id="python_solutions.tests.test_Deque.test_pop_front_works_for_deque"></a>

#### test\_pop\_front\_works\_for\_deque

```python
def test_pop_front_works_for_deque(d)
```

<a id="python_solutions.tests.test_Deque.test_pop_back_works_for_deque"></a>

#### test\_pop\_back\_works\_for\_deque

```python
def test_pop_back_works_for_deque(d)
```

<a id="python_solutions.tests.test_digit_sort.random"></a>

## random

<a id="python_solutions.tests.test_digit_sort.pytest"></a>

## pytest

<a id="python_solutions.tests.test_digit_sort.restore_to_nums"></a>

## restore\_to\_nums

<a id="python_solutions.tests.test_digit_sort.to_m_based"></a>

## to\_m\_based

<a id="python_solutions.tests.test_digit_sort.number"></a>

#### number

```python
@pytest.fixture()
def number()
```

<a id="python_solutions.tests.test_digit_sort.test_to_m_based_array"></a>

#### test\_to\_m\_based\_array

```python
def test_to_m_based_array(number)
```

<a id="python_solutions.tests.test_digit_sort.test_restore_to_nums"></a>

#### test\_restore\_to\_nums

```python
def test_restore_to_nums(number)
```

<a id="python_solutions.tests.test_DoubleNode.DoubleNode"></a>

## DoubleNode

<a id="python_solutions.tests.test_DoubleNode.prev"></a>

## prev

<a id="python_solutions.tests.test_DoubleNode.pytest"></a>

## pytest

<a id="python_solutions.tests.test_DoubleNode.dn"></a>

#### dn

```python
@pytest.fixture()
def dn()
```

<a id="python_solutions.tests.test_DoubleNode.test_doublenode_prev"></a>

#### test\_doublenode\_prev

```python
def test_doublenode_prev(dn)
```

<a id="python_solutions.tests.test_DoubleNode.test_doublenode_next"></a>

#### test\_doublenode\_next

```python
def test_doublenode_next(dn)
```

<a id="python_solutions.tests.test_DoubleNode.test_doublenode_str"></a>

#### test\_doublenode\_str

```python
def test_doublenode_str(dn)
```

<a id="python_solutions.tests.test_DoubleNode.test_doublenode_initialization_without_data_gives_blank_node"></a>

#### test\_doublenode\_initialization\_without\_data\_gives\_blank\_node

```python
def test_doublenode_initialization_without_data_gives_blank_node(dn)
```

<a id="python_solutions.tests.test_DoubleNode.test_raises_error_when_init_with_wrong_next_node"></a>

#### test\_raises\_error\_when\_init\_with\_wrong\_next\_node

```python
def test_raises_error_when_init_with_wrong_next_node()
```

<a id="python_solutions.tests.test_DoubleNode.test_raises_error_when_init_with_wrong_prev_node"></a>

#### test\_raises\_error\_when\_init\_with\_wrong\_prev\_node

```python
def test_raises_error_when_init_with_wrong_prev_node()
```

<a id="python_solutions.tests.test_DoubleNode.test_raises_error_when_trying_to_assign_wrong_prev_node"></a>

#### test\_raises\_error\_when\_trying\_to\_assign\_wrong\_prev\_node

```python
def test_raises_error_when_trying_to_assign_wrong_prev_node()
```

<a id="python_solutions.tests.test_dynamic_programmimg.pytest"></a>

## pytest

<a id="python_solutions.tests.test_dynamic_programmimg.subprocess"></a>

## subprocess

<a id="python_solutions.tests.test_dynamic_programmimg.random"></a>

## random

<a id="python_solutions.tests.test_dynamic_programmimg.string"></a>

## string

<a id="python_solutions.tests.test_dynamic_programmimg.c_int"></a>

## c\_int

<a id="python_solutions.tests.test_dynamic_programmimg.POINTER"></a>

## POINTER

<a id="python_solutions.tests.test_dynamic_programmimg.CDLL"></a>

## CDLL

<a id="python_solutions.tests.test_dynamic_programmimg.c_char"></a>

## c\_char

<a id="python_solutions.tests.test_dynamic_programmimg.DynamicProgrammingProblem"></a>

## DynamicProgrammingProblem

<a id="python_solutions.tests.test_dynamic_programmimg.KnapsackProblem"></a>

## KnapsackProblem

<a id="python_solutions.tests.test_dynamic_programmimg.DamerauLevensteinDistance"></a>

## DamerauLevensteinDistance

<a id="python_solutions.tests.test_dynamic_programmimg.LongestCommonSubsequence"></a>

## LongestCommonSubsequence

<a id="python_solutions.tests.test_dynamic_programmimg.LongestIncreasingSubsequence"></a>

## LongestIncreasingSubsequence

<a id="python_solutions.tests.test_dynamic_programmimg.maxSubarraySum"></a>

## maxSubarraySum

<a id="python_solutions.tests.test_dynamic_programmimg.TravellingSalesmanProblem"></a>

## TravellingSalesmanProblem

<a id="python_solutions.tests.test_dynamic_programmimg.test_dp_class_solve_raises"></a>

#### test\_dp\_class\_solve\_raises

```python
def test_dp_class_solve_raises()
```

<a id="python_solutions.tests.test_dynamic_programmimg.generate_test_cases_with_output_for_knapsack"></a>

#### generate\_test\_cases\_with\_output\_for\_knapsack

```python
def generate_test_cases_with_output_for_knapsack(n_start=5,
                                                 n_end=100,
                                                 r_start=10,
                                                 r_end=1000,
                                                 t_start=1,
                                                 t_end=16,
                                                 i_start=0,
                                                 i_end=200,
                                                 S_start=100,
                                                 S_end=2000)
```

<a id="python_solutions.tests.test_dynamic_programmimg.generate_test_cases"></a>

#### generate\_test\_cases

```python
def generate_test_cases(function, amount=20)
```

<a id="python_solutions.tests.test_dynamic_programmimg.test_knapsack_problem"></a>

#### test\_knapsack\_problem

```python
@pytest.mark.parametrize(
    "test_input, test_output",
    generate_test_cases(generate_test_cases_with_output_for_knapsack, 20) + [
        # bounds
        (([], [], 0), 0),
        (([12], [1], 0), 0),
        (([15, 1, 12], [10000, 1, 0], 14), 1)
    ])
def test_knapsack_problem(test_input, test_output)
```

<a id="python_solutions.tests.test_dynamic_programmimg.test_damerau_levenstein_bounds"></a>

#### test\_damerau\_levenstein\_bounds

```python
def test_damerau_levenstein_bounds()
```

<a id="python_solutions.tests.test_dynamic_programmimg.generate_test_cases_with_output_for_damerau_levenstein"></a>

#### generate\_test\_cases\_with\_output\_for\_damerau\_levenstein

```python
def generate_test_cases_with_output_for_damerau_levenstein(
        str1_len=10, str2_len=10)
```

<a id="python_solutions.tests.test_dynamic_programmimg.test_damerau_levenstein"></a>

#### test\_damerau\_levenstein

```python
@pytest.mark.parametrize(
    "test_input, test_output",
    generate_test_cases(generate_test_cases_with_output_for_damerau_levenstein,
                        20) + [
                            (('', ''), 0),
                            # transpositional check
                            (('10', '01'), 1),
                            (('011', '101'), 1),
                            (('1023456789', '01wertyuio'), 9),
                            (('abcdef', 'abcfad'), 3)
                        ])
def test_damerau_levenstein(test_input, test_output)
```

<a id="python_solutions.tests.test_dynamic_programmimg.test_lcs_symmetry"></a>

#### test\_lcs\_symmetry

```python
def test_lcs_symmetry()
```

<a id="python_solutions.tests.test_dynamic_programmimg.test_some_lcs_test_cases"></a>

#### test\_some\_lcs\_test\_cases

```python
@pytest.mark.parametrize(
    'test_input, test_output',
    [
        (('workattech', 'branch'), 4),
        (('helloworld', 'playword'), 5),
        (('hello', 'hello'), 5),
        (('abc', 'def'), 0),
        # bounds
        (('', ''), 0),
        (('abc', ''), 0),
        (('', 'abc'), 0),
        (('abc', 'abc'), 3)
    ])
def test_some_lcs_test_cases(test_input, test_output)
```

<a id="python_solutions.tests.test_dynamic_programmimg.test_some_lis_test_cases"></a>

#### test\_some\_lis\_test\_cases

```python
@pytest.mark.parametrize(
    'test_input, test_output',
    [(([10, 20, 2, 5, 3, 8, 8, 25, 6]), 4),
     (([10, -63, 7, -50, 32, -9, -3]), 4), (([71, 0, 4, 42, -31, 4, -42]), 3),
     (([77, 0, -2, 25, 1, 70]), 3), (([2, 2, 1, 5, 7, -50, 80]), 4),
     (([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]), 6),
     (([5, 8, 3, 7, 9, 1]), 3), (([]), 0), (([random.randint(0, 100)]), 1),
     (([1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10),
     ((1, 0, 2, 3, 4, 5, 6, 7, 8, 10, 9), 9)])
def test_some_lis_test_cases(test_input, test_output)
```

<a id="python_solutions.tests.test_dynamic_programmimg.arr"></a>

#### arr

<a id="python_solutions.tests.test_dynamic_programmimg.queries"></a>

#### queries

<a id="python_solutions.tests.test_dynamic_programmimg.test_max_subarray_sum_init"></a>

#### test\_max\_subarray\_sum\_init

```python
@pytest.mark.parametrize('arr, queries', [(arr, queries)])
def test_max_subarray_sum_init(arr, queries)
```

<a id="python_solutions.tests.test_dynamic_programmimg.test_max_subarray_sum_solve"></a>

#### test\_max\_subarray\_sum\_solve

```python
@pytest.mark.parametrize('arr, queries', [(arr, queries)])
def test_max_subarray_sum_solve(arr, queries)
```

<a id="python_solutions.tests.test_dynamic_programmimg.test_max_subarray_sum_empty"></a>

#### test\_max\_subarray\_sum\_empty

```python
@pytest.mark.parametrize('arr, queries', [([], [])])
def test_max_subarray_sum_empty(arr, queries)
```

<a id="python_solutions.tests.test_dynamic_programmimg.test_max_subarray_sum_one"></a>

#### test\_max\_subarray\_sum\_one

```python
@pytest.mark.parametrize('arr, queries', [([5], [(0, 0)])])
def test_max_subarray_sum_one(arr, queries)
```

<a id="python_solutions.tests.test_dynamic_programmimg.test_travelling_salesman"></a>

#### test\_travelling\_salesman

```python
def test_travelling_salesman()
```

<a id="python_solutions.tests.test_edit_distance.pytest"></a>

## pytest

<a id="python_solutions.tests.test_edit_distance.edit_distance"></a>

## edit\_distance

<a id="python_solutions.tests.test_edit_distance.jaro_distance"></a>

## jaro\_distance

<a id="python_solutions.tests.test_edit_distance.hamming_distance"></a>

## hamming\_distance

<a id="python_solutions.tests.test_edit_distance.test_jaro_distance"></a>

#### test\_jaro\_distance

```python
@pytest.mark.parametrize(
    'str1, str2, output',
    [
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
def test_jaro_distance(str1, str2, output)
```

<a id="python_solutions.tests.test_edit_distance.test_hamming_distance"></a>

#### test\_hamming\_distance

```python
@pytest.mark.parametrize("input1, input2, output",
                         [("karolin", "kathrin", 3),
                          ("karolina", "kathrine", 4),
                          ("1011101", "1001001", 2)])
def test_hamming_distance(input1, input2, output)
```

<a id="python_solutions.tests.test_edit_distance.test_hamming_error"></a>

#### test\_hamming\_error

```python
def test_hamming_error()
```

<a id="python_solutions.tests.test_edit_distance.test_edit_distance"></a>

#### test\_edit\_distance

```python
@pytest.mark.parametrize("input1, input2, method, expected",
                         [("hello", "holla", "jaro", 0.73333333),
                          ("apple", "banana", "jaro", 0.45555555),
                          ("karolin", "kathrin", "hamming", 3),
                          ("karolina", "kathrine", "hamming", 4),
                          ("kitten", "sitting", "dl", 3),
                          ("flaw", "lawn", "dl", 2),
                          ("kitten", "sitting", "lcs", 4),
                          ("flaw", "lawn", "lcs", 3)])
def test_edit_distance(input1, input2, method, expected)
```

<a id="python_solutions.tests.test_graph.pytest"></a>

## pytest

<a id="python_solutions.tests.test_graph.copy"></a>

## copy

<a id="python_solutions.tests.test_graph.logging"></a>

## logging

<a id="python_solutions.tests.test_graph.random"></a>

## random

<a id="python_solutions.tests.test_graph.GraphNode"></a>

## GraphNode

<a id="python_solutions.tests.test_graph.WeightedGraphNode"></a>

## WeightedGraphNode

<a id="python_solutions.tests.test_graph.Edge"></a>

## Edge

<a id="python_solutions.tests.test_graph.Graph"></a>

## Graph

<a id="python_solutions.tests.test_graph.WeightedGraph"></a>

## WeightedGraph

<a id="python_solutions.tests.test_graph.test_can_create_everything"></a>

#### test\_can\_create\_everything

```python
def test_can_create_everything()
```

<a id="python_solutions.tests.test_graph.test_undirected_graph_node_workes_well"></a>

#### test\_undirected\_graph\_node\_workes\_well

```python
def test_undirected_graph_node_workes_well()
```

<a id="python_solutions.tests.test_graph.graphs"></a>

#### graphs

```python
@pytest.fixture
def graphs()
```

<a id="python_solutions.tests.test_graph.nodes"></a>

#### nodes

```python
@pytest.fixture
def nodes()
```

<a id="python_solutions.tests.test_graph.test_graphs_can_accept_vertex"></a>

#### test\_graphs\_can\_accept\_vertex

```python
def test_graphs_can_accept_vertex(graphs, nodes)
```

<a id="python_solutions.tests.test_graph.nodes2"></a>

#### nodes2

```python
@pytest.fixture
def nodes2()
```

<a id="python_solutions.tests.test_graph.test_graphs_can_accept_two_unconnected_vertices"></a>

#### test\_graphs\_can\_accept\_two\_unconnected\_vertices

```python
def test_graphs_can_accept_two_unconnected_vertices(graphs, nodes, nodes2)
```

<a id="python_solutions.tests.test_graph.test_find_kwarg_data"></a>

#### test\_find\_kwarg\_data

```python
def test_find_kwarg_data(graphs, nodes)
```

<a id="python_solutions.tests.test_graph.test_find_kwarg_with_edges"></a>

#### test\_find\_kwarg\_with\_edges

```python
def test_find_kwarg_with_edges(graphs, nodes)
```

<a id="python_solutions.tests.test_graph.uncon2"></a>

#### uncon2

```python
@pytest.fixture
def uncon2(graphs, nodes, nodes2)
```

<a id="python_solutions.tests.test_graph.test_can_remove_vertices_by_index"></a>

#### test\_can\_remove\_vertices\_by\_index

```python
@pytest.mark.parametrize('index_rem, all_vertices, first', [(0, ['4'], '4'),
                                                            (1, ['3'], '3')])
def test_can_remove_vertices_by_index(uncon2, index_rem, all_vertices, first)
```

<a id="python_solutions.tests.test_graph.test_can_remove_vertices_by_data"></a>

#### test\_can\_remove\_vertices\_by\_data

```python
@pytest.mark.parametrize('data_rem, all_vertices, first, second, index',
                         [(3, ['4'], '4', 4, 1), (4, ['3'], '3', 3, 0)])
def test_can_remove_vertices_by_data(uncon2, data_rem, all_vertices, first,
                                     second, index)
```

<a id="python_solutions.tests.test_graph.test_raises_when_no_data_or_index_specified_in_remove"></a>

#### test\_raises\_when\_no\_data\_or\_index\_specified\_in\_remove

```python
def test_raises_when_no_data_or_index_specified_in_remove(uncon2)
```

<a id="python_solutions.tests.test_graph.test_add_edge_between_vertices_undir"></a>

#### test\_add\_edge\_between\_vertices\_undir

```python
@pytest.mark.parametrize('front, back', [(0, 1), (1, 0)])
def test_add_edge_between_vertices_undir(uncon2, front, back)
```

<a id="python_solutions.tests.test_graph.test_add_edge_between_vertices_wei"></a>

#### test\_add\_edge\_between\_vertices\_wei

```python
@pytest.mark.parametrize('direction, weight', [(0, 3), (0, []), (1, 4),
                                               (1, [])])
def test_add_edge_between_vertices_wei(uncon2, direction, weight)
```

<a id="python_solutions.tests.test_graph.test_graphs_can_accept_two_connected_vertices"></a>

#### test\_graphs\_can\_accept\_two\_connected\_vertices

```python
def test_graphs_can_accept_two_connected_vertices(graphs, nodes)
```

<a id="python_solutions.tests.test_graph.con2"></a>

#### con2

```python
@pytest.fixture
def con2(graphs)
```

<a id="python_solutions.tests.test_graph.test_remove_edge"></a>

#### test\_remove\_edge

```python
@pytest.mark.parametrize('front, back', [(0, 1), (1, 0)])
def test_remove_edge(con2, front, back)
```

<a id="python_solutions.tests.test_graph.test_remove_vertex"></a>

#### test\_remove\_vertex

```python
@pytest.mark.parametrize('params', [({
    'index': 0
}), ({
    'index': 1
}), ({
    'data': 3
}), ({
    'data': 4
})])
def test_remove_vertex(con2, params)
```

<a id="python_solutions.tests.test_graph.test_add_vertices_manipulate_edges_remove_vertices"></a>

#### test\_add\_vertices\_manipulate\_edges\_remove\_vertices

```python
def test_add_vertices_manipulate_edges_remove_vertices()
```

<a id="python_solutions.tests.test_graph.weights"></a>

#### weights

<a id="python_solutions.tests.test_graph.con5"></a>

#### con5

```python
@pytest.fixture
def con5()
```

<a id="python_solutions.tests.test_graph.bfs_graph"></a>

#### bfs\_graph

```python
@pytest.fixture
def bfs_graph()
```

<a id="python_solutions.tests.test_graph.test_bfs"></a>

#### test\_bfs

```python
def test_bfs(uncon2, con2, con5, bfs_graph)
```

<a id="python_solutions.tests.test_graph.test_adjancency_matrix"></a>

#### test\_adjancency\_matrix

```python
def test_adjancency_matrix(con5)
```

<a id="python_solutions.tests.test_graph.test_cycles_detector"></a>

#### test\_cycles\_detector

```python
def test_cycles_detector(uncon2, con5, bfs_graph)
```

<a id="python_solutions.tests.test_graph.test_topo_sort"></a>

#### test\_topo\_sort

```python
def test_topo_sort(bfs_graph)
```

<a id="python_solutions.tests.test_graph.test_single_node"></a>

#### test\_single\_node

```python
def test_single_node()
```

<a id="python_solutions.tests.test_graph.test_two_nodes_no_edge"></a>

#### test\_two\_nodes\_no\_edge

```python
def test_two_nodes_no_edge()
```

<a id="python_solutions.tests.test_graph.test_simple_cycle"></a>

#### test\_simple\_cycle

```python
def test_simple_cycle()
```

<a id="python_solutions.tests.test_graph.graph"></a>

#### graph

```python
@pytest.fixture
def graph()
```

<a id="python_solutions.tests.test_graph.test_multiple_scc"></a>

#### test\_multiple\_scc

```python
def test_multiple_scc(graph)
```

<a id="python_solutions.tests.test_graph.test_complex_graph"></a>

#### test\_complex\_graph

```python
def test_complex_graph(graph)
```

<a id="python_solutions.tests.test_graph.test_edge_cases"></a>

#### test\_edge\_cases

```python
def test_edge_cases()
```

<a id="python_solutions.tests.test_graph.test_dijkstra_undir"></a>

#### test\_dijkstra\_undir

```python
@pytest.mark.parametrize('graph_type', [Graph, WeightedGraph])
def test_dijkstra_undir(graph_type)
```

<a id="python_solutions.tests.test_graph.test_bellman_ford"></a>

#### test\_bellman\_ford

```python
def test_bellman_ford()
```

<a id="python_solutions.tests.test_graph.test_simple_flow"></a>

#### test\_simple\_flow

```python
@pytest.mark.parametrize('algo', ['dinics', 'gt'])
def test_simple_flow(graph, algo)
```

<a id="python_solutions.tests.test_graph.test_multiple_flows"></a>

#### test\_multiple\_flows

```python
@pytest.mark.parametrize('algo', ['dinics', 'gt'])
def test_multiple_flows(graph, algo)
```

<a id="python_solutions.tests.test_graph.test_no_flow"></a>

#### test\_no\_flow

```python
@pytest.mark.parametrize('algo', ['dinics', 'gt'])
def test_no_flow(algo)
```

<a id="python_solutions.tests.test_graph.test_max_flow"></a>

#### test\_max\_flow

```python
@pytest.mark.parametrize('algo', ['dinics', 'gt'])
def test_max_flow(graph, algo)
```

<a id="python_solutions.tests.test_graph.test_backflow"></a>

#### test\_backflow

```python
@pytest.mark.parametrize('algo', ['dinics', 'gt'])
def test_backflow(graph, algo)
```

<a id="python_solutions.tests.test_graph.test_algorithm_mst_correctness"></a>

#### test\_algorithm\_mst\_correctness

```python
@pytest.mark.parametrize('algo', ['prims', 'kruskals'])
def test_algorithm_mst_correctness(algo)
```

<a id="python_solutions.tests.test_graph.test_algorithm_mst_disconnected_graph"></a>

#### test\_algorithm\_mst\_disconnected\_graph

```python
@pytest.mark.parametrize('algo', ['prims'])
def test_algorithm_mst_disconnected_graph(algo)
```

<a id="python_solutions.tests.test_graph.test_algorithm_mst_empty_graph"></a>

#### test\_algorithm\_mst\_empty\_graph

```python
@pytest.mark.parametrize('algo', ['prims', 'kruskals'])
def test_algorithm_mst_empty_graph(algo)
```

<a id="python_solutions.tests.test_graph.test_algorithm_mst_uniform_weights"></a>

#### test\_algorithm\_mst\_uniform\_weights

```python
@pytest.mark.parametrize('algo', ['prims', 'kruskals'])
def test_algorithm_mst_uniform_weights(algo)
```

<a id="python_solutions.tests.test_graph.test_mst_complex_graph"></a>

#### test\_mst\_complex\_graph

```python
def test_mst_complex_graph()
```

<a id="python_solutions.tests.test_graph.test_graph_vertices_and_edges_coloring"></a>

#### test\_graph\_vertices\_and\_edges\_coloring

```python
def test_graph_vertices_and_edges_coloring()
```

<a id="python_solutions.tests.test_graph.test_complex_graph_coloring"></a>

#### test\_complex\_graph\_coloring

```python
def test_complex_graph_coloring()
```

<a id="python_solutions.tests.test_hashtable.HashTable_closed"></a>

## HashTable\_closed

<a id="python_solutions.tests.test_hashtable.gen_primes"></a>

## gen\_primes

<a id="python_solutions.tests.test_hashtable.HashTable_open"></a>

## HashTable\_open

<a id="python_solutions.tests.test_hashtable.poly_hash"></a>

## poly\_hash

<a id="python_solutions.tests.test_hashtable.random"></a>

## random

<a id="python_solutions.tests.test_hashtable.pytest"></a>

## pytest

<a id="python_solutions.tests.test_hashtable.test_gen_primes"></a>

#### test\_gen\_primes

```python
def test_gen_primes()
```

<a id="python_solutions.tests.test_hashtable.test_hashtable_closed_runs"></a>

#### test\_hashtable\_closed\_runs

```python
def test_hashtable_closed_runs()
```

<a id="python_solutions.tests.test_hashtable.ht"></a>

#### ht

```python
@pytest.fixture()
def ht()
```

<a id="python_solutions.tests.test_hashtable.test_setter_in_hashtable_for_the_first_element"></a>

#### test\_setter\_in\_hashtable\_for\_the\_first\_element

```python
def test_setter_in_hashtable_for_the_first_element(ht)
```

<a id="python_solutions.tests.test_hashtable.test_setter_in_hashtable_for_the_second_element"></a>

#### test\_setter\_in\_hashtable\_for\_the\_second\_element

```python
def test_setter_in_hashtable_for_the_second_element(ht)
```

<a id="python_solutions.tests.test_hashtable.test_ht_handles_collisions"></a>

#### test\_ht\_handles\_collisions

```python
def test_ht_handles_collisions(ht)
```

<a id="python_solutions.tests.test_hashtable.test_cannot_set_size_and_capacity_for_ht_after_init"></a>

#### test\_cannot\_set\_size\_and\_capacity\_for\_ht\_after\_init

```python
def test_cannot_set_size_and_capacity_for_ht_after_init(ht)
```

<a id="python_solutions.tests.test_hashtable.ht_with_samples"></a>

#### ht\_with\_samples

```python
@pytest.fixture()
def ht_with_samples(ht)
```

<a id="python_solutions.tests.test_hashtable.test_property_pairs_getter"></a>

#### test\_property\_pairs\_getter

```python
def test_property_pairs_getter(ht_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_property_pairs_setitem"></a>

#### test\_property\_pairs\_setitem

```python
def test_property_pairs_setitem(ht_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_property_pairs_setter"></a>

#### test\_property\_pairs\_setter

```python
def test_property_pairs_setter(ht_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_deletion_in_ht"></a>

#### test\_deletion\_in\_ht

```python
def test_deletion_in_ht(ht_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_update_in_ht"></a>

#### test\_update\_in\_ht

```python
def test_update_in_ht(ht_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_to_dict_closed"></a>

#### test\_to\_dict\_closed

```python
def test_to_dict_closed(ht_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_search_in_ht"></a>

#### test\_search\_in\_ht

```python
def test_search_in_ht(ht_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_contains_in_ht"></a>

#### test\_contains\_in\_ht

```python
def test_contains_in_ht(ht_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_getitem_raises_for_absent_element"></a>

#### test\_getitem\_raises\_for\_absent\_element

```python
def test_getitem_raises_for_absent_element(ht_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_str_and_repr"></a>

#### test\_str\_and\_repr

```python
def test_str_and_repr(ht_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_from_dict"></a>

#### test\_from\_dict

```python
def test_from_dict(ht_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_ht_with_different_hashes"></a>

#### test\_ht\_with\_different\_hashes

```python
def test_ht_with_different_hashes()
```

<a id="python_solutions.tests.test_hashtable.test_ht_with_poly_hash_as_callable"></a>

#### test\_ht\_with\_poly\_hash\_as\_callable

```python
def test_ht_with_poly_hash_as_callable()
```

<a id="python_solutions.tests.test_hashtable.test_can_create_ht_open"></a>

#### test\_can\_create\_ht\_open

```python
def test_can_create_ht_open()
```

<a id="python_solutions.tests.test_hashtable.ht_open"></a>

#### ht\_open

```python
@pytest.fixture()
def ht_open()
```

<a id="python_solutions.tests.test_hashtable.test_setitem_and_getitem_in_ht"></a>

#### test\_setitem\_and\_getitem\_in\_ht

```python
def test_setitem_and_getitem_in_ht(ht_open)
```

<a id="python_solutions.tests.test_hashtable.ht_open_with_samples"></a>

#### ht\_open\_with\_samples

```python
@pytest.fixture
def ht_open_with_samples(ht_open)
```

<a id="python_solutions.tests.test_hashtable.test_property_elements_defensive_copy"></a>

#### test\_property\_elements\_defensive\_copy

```python
def test_property_elements_defensive_copy(ht_open_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_property_elements_setitem"></a>

#### test\_property\_elements\_setitem

```python
def test_property_elements_setitem(ht_open_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_set_elements"></a>

#### test\_set\_elements

```python
def test_set_elements(ht_open_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_update_in_ht_open"></a>

#### test\_update\_in\_ht\_open

```python
def test_update_in_ht_open(ht_open_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_errors_in_update_and_getitem"></a>

#### test\_errors\_in\_update\_and\_getitem

```python
def test_errors_in_update_and_getitem(ht_open_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_search_returns_false_when_no_elements_found"></a>

#### test\_search\_returns\_false\_when\_no\_elements\_found

```python
def test_search_returns_false_when_no_elements_found(ht_open_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_to_dict_open"></a>

#### test\_to\_dict\_open

```python
def test_to_dict_open(ht_open)
```

<a id="python_solutions.tests.test_hashtable_stresses.pytest"></a>

## pytest

<a id="python_solutions.tests.test_hashtable_stresses.HashTable_closed"></a>

## HashTable\_closed

<a id="python_solutions.tests.test_hashtable_stresses.HashTable_open"></a>

## HashTable\_open

<a id="python_solutions.tests.test_hashtable_stresses.ht"></a>

#### ht

```python
@pytest.fixture()
def ht()
```

<a id="python_solutions.tests.test_hashtable_stresses.test_stress_ht_closed"></a>

#### test\_stress\_ht\_closed

```python
def test_stress_ht_closed(ht)
```

<a id="python_solutions.tests.test_hashtable_stresses.ht_open"></a>

#### ht\_open

```python
@pytest.fixture()
def ht_open()
```

<a id="python_solutions.tests.test_hashtable_stresses.test_stress_ht_open"></a>

#### test\_stress\_ht\_open

```python
def test_stress_ht_open(ht_open)
```

<a id="python_solutions.tests.test_heap.random"></a>

## random

<a id="python_solutions.tests.test_heap.logging"></a>

## logging

<a id="python_solutions.tests.test_heap.pytest"></a>

## pytest

<a id="python_solutions.tests.test_heap.Heap"></a>

## Heap

<a id="python_solutions.tests.test_heap.heap_sort"></a>

## heap\_sort

<a id="python_solutions.tests.test_heap.test_can_create_heap"></a>

#### test\_can\_create\_heap

```python
def test_can_create_heap()
```

<a id="python_solutions.tests.test_heap.test_boundary_cases"></a>

#### test\_boundary\_cases

```python
def test_boundary_cases()
```

<a id="python_solutions.tests.test_heap.test_heap_sort"></a>

#### test\_heap\_sort

```python
def test_heap_sort()
```

<a id="python_solutions.tests.test_heap.test_repr"></a>

#### test\_repr

```python
def test_repr()
```

<a id="python_solutions.tests.test_hyperloglog.pytest"></a>

## pytest

<a id="python_solutions.tests.test_hyperloglog.HyperLogLog"></a>

## HyperLogLog

<a id="python_solutions.tests.test_hyperloglog.test_can_create_hyperloglog"></a>

#### test\_can\_create\_hyperloglog

```python
def test_can_create_hyperloglog()
```

<a id="python_solutions.tests.test_hyperloglog.test_cardinality"></a>

#### test\_cardinality

```python
@pytest.mark.parametrize(
    'precision, length',
    [
        (14, 10),
        (18, 50000)  #,
        #(25, 5000000)
    ])
def test_cardinality(precision, length)
```

<a id="python_solutions.tests.test_insert_sort.random"></a>

## random

<a id="python_solutions.tests.test_insert_sort.patch"></a>

## patch

<a id="python_solutions.tests.test_insert_sort.test_import_error_for_quick"></a>

#### test\_import\_error\_for\_quick

```python
def test_import_error_for_quick()
```

<a id="python_solutions.tests.test_insert_sort.test_quick_sort_median_of_medians"></a>

#### test\_quick\_sort\_median\_of\_medians

```python
def test_quick_sort_median_of_medians()
```

<a id="python_solutions.tests.test_LinkedList.LinkedList"></a>

## LinkedList

<a id="python_solutions.tests.test_LinkedList.Node"></a>

## Node

<a id="python_solutions.tests.test_LinkedList.pytest"></a>

## pytest

<a id="python_solutions.tests.test_LinkedList.test_can_create_blank_linkedlist"></a>

#### test\_can\_create\_blank\_linkedlist

```python
def test_can_create_blank_linkedlist()
```

<a id="python_solutions.tests.test_LinkedList.blank_ll"></a>

#### blank\_ll

```python
@pytest.fixture()
def blank_ll()
```

<a id="python_solutions.tests.test_LinkedList.test_no_nodes_size_of_ll_exists"></a>

#### test\_no\_nodes\_size\_of\_ll\_exists

```python
def test_no_nodes_size_of_ll_exists(blank_ll)
```

<a id="python_solutions.tests.test_LinkedList.test_no_nodes_head_of_ll_exists"></a>

#### test\_no\_nodes\_head\_of\_ll\_exists

```python
def test_no_nodes_head_of_ll_exists(blank_ll)
```

<a id="python_solutions.tests.test_LinkedList.test_no_nodes_tail_of_ll_exists"></a>

#### test\_no\_nodes\_tail\_of\_ll\_exists

```python
def test_no_nodes_tail_of_ll_exists(blank_ll)
```

<a id="python_solutions.tests.test_LinkedList.test_can_not_modify_tail_manually"></a>

#### test\_can\_not\_modify\_tail\_manually

```python
def test_can_not_modify_tail_manually(blank_ll)
```

<a id="python_solutions.tests.test_LinkedList.test_can_not_modify_size_manually"></a>

#### test\_can\_not\_modify\_size\_manually

```python
def test_can_not_modify_size_manually(blank_ll)
```

<a id="python_solutions.tests.test_LinkedList.ll_with_node"></a>

#### ll\_with\_node

```python
@pytest.fixture()
def ll_with_node()
```

<a id="python_solutions.tests.test_LinkedList.ll_with_same_head_and_tail"></a>

#### ll\_with\_same\_head\_and\_tail

```python
@pytest.fixture()
def ll_with_same_head_and_tail()
```

<a id="python_solutions.tests.test_LinkedList.test_size_ll_with_1_node_initialized_differently"></a>

#### test\_size\_ll\_with\_1\_node\_initialized\_differently

```python
def test_size_ll_with_1_node_initialized_differently(
        ll_with_same_head_and_tail)
```

<a id="python_solutions.tests.test_LinkedList.test_head_and_tail_in_ll_with_1_node"></a>

#### test\_head\_and\_tail\_in\_ll\_with\_1\_node

```python
def test_head_and_tail_in_ll_with_1_node(ll_with_same_head_and_tail)
```

<a id="python_solutions.tests.test_LinkedList.test_one_node_ll_has_size"></a>

#### test\_one\_node\_ll\_has\_size

```python
def test_one_node_ll_has_size(ll_with_node)
```

<a id="python_solutions.tests.test_LinkedList.test_size1_ll_has_equal_head_and_tail"></a>

#### test\_size1\_ll\_has\_equal\_head\_and\_tail

```python
def test_size1_ll_has_equal_head_and_tail(ll_with_node)
```

<a id="python_solutions.tests.test_LinkedList.test_can_initialize_ll_from_chain_of_nodes_using_head"></a>

#### test\_can\_initialize\_ll\_from\_chain\_of\_nodes\_using\_head

```python
def test_can_initialize_ll_from_chain_of_nodes_using_head()
```

<a id="python_solutions.tests.test_LinkedList.ll_with_2_nodes_from_head"></a>

#### ll\_with\_2\_nodes\_from\_head

```python
@pytest.fixture()
def ll_with_2_nodes_from_head()
```

<a id="python_solutions.tests.test_LinkedList.test_size_for_ll_with_2_nodes_is_2"></a>

#### test\_size\_for\_ll\_with\_2\_nodes\_is\_2

```python
def test_size_for_ll_with_2_nodes_is_2(ll_with_2_nodes_from_head)
```

<a id="python_solutions.tests.test_LinkedList.test_head_determines_correctly_for_ll_with_2_nodes"></a>

#### test\_head\_determines\_correctly\_for\_ll\_with\_2\_nodes

```python
def test_head_determines_correctly_for_ll_with_2_nodes(
        ll_with_2_nodes_from_head)
```

<a id="python_solutions.tests.test_LinkedList.test_tail_determines_correctly_for_ll_with_2_nodes"></a>

#### test\_tail\_determines\_correctly\_for\_ll\_with\_2\_nodes

```python
def test_tail_determines_correctly_for_ll_with_2_nodes(
        ll_with_2_nodes_from_head)
```

<a id="python_solutions.tests.test_LinkedList.test_ll_from_chain_of_nodes_using_tail_leads_to_blank_ll"></a>

#### test\_ll\_from\_chain\_of\_nodes\_using\_tail\_leads\_to\_blank\_ll

```python
def test_ll_from_chain_of_nodes_using_tail_leads_to_blank_ll()
```

<a id="python_solutions.tests.test_LinkedList.ll_with_2_nodes_from_tail"></a>

#### ll\_with\_2\_nodes\_from\_tail

```python
@pytest.fixture()
def ll_with_2_nodes_from_tail()
```

<a id="python_solutions.tests.test_LinkedList.test_size_for_ll_with_2_nodes_from_tail_is_0"></a>

#### test\_size\_for\_ll\_with\_2\_nodes\_from\_tail\_is\_0

```python
def test_size_for_ll_with_2_nodes_from_tail_is_0(ll_with_2_nodes_from_tail)
```

<a id="python_solutions.tests.test_LinkedList.test_head_of_ll_with_2_nodes_from_tail_is_none"></a>

#### test\_head\_of\_ll\_with\_2\_nodes\_from\_tail\_is\_none

```python
def test_head_of_ll_with_2_nodes_from_tail_is_none(ll_with_2_nodes_from_tail)
```

<a id="python_solutions.tests.test_LinkedList.test_tail_of_ll_with_2_nodes_from_tail_is_none"></a>

#### test\_tail\_of\_ll\_with\_2\_nodes\_from\_tail\_is\_none

```python
def test_tail_of_ll_with_2_nodes_from_tail_is_none(ll_with_2_nodes_from_tail)
```

<a id="python_solutions.tests.test_LinkedList.test_iter_in_ll_works"></a>

#### test\_iter\_in\_ll\_works

```python
def test_iter_in_ll_works()
```

<a id="python_solutions.tests.test_LinkedList.test_append_in_ll_works"></a>

#### test\_append\_in\_ll\_works

```python
def test_append_in_ll_works()
```

<a id="python_solutions.tests.test_LinkedList.test_insertion_of_the_first_element_in_ll_works"></a>

#### test\_insertion\_of\_the\_first\_element\_in\_ll\_works

```python
def test_insertion_of_the_first_element_in_ll_works()
```

<a id="python_solutions.tests.test_LinkedList.test_insertion_in_the_head_in_ll_works"></a>

#### test\_insertion\_in\_the\_head\_in\_ll\_works

```python
def test_insertion_in_the_head_in_ll_works()
```

<a id="python_solutions.tests.test_LinkedList.test_append_by_insertion_in_ll_works"></a>

#### test\_append\_by\_insertion\_in\_ll\_works

```python
def test_append_by_insertion_in_ll_works()
```

<a id="python_solutions.tests.test_LinkedList.test_actual_insertion_in_ll_works"></a>

#### test\_actual\_insertion\_in\_ll\_works

```python
def test_actual_insertion_in_ll_works()
```

<a id="python_solutions.tests.test_LinkedList.ll_for_erase"></a>

#### ll\_for\_erase

```python
@pytest.fixture()
def ll_for_erase()
```

<a id="python_solutions.tests.test_LinkedList.test_delete_head_element_in_ll_works"></a>

#### test\_delete\_head\_element\_in\_ll\_works

```python
def test_delete_head_element_in_ll_works(ll_for_erase)
```

<a id="python_solutions.tests.test_LinkedList.test_delete_the_last_element_in_ll_works"></a>

#### test\_delete\_the\_last\_element\_in\_ll\_works

```python
def test_delete_the_last_element_in_ll_works(ll_for_erase)
```

<a id="python_solutions.tests.test_LinkedList.test_delete_only_element_in_ll"></a>

#### test\_delete\_only\_element\_in\_ll

```python
def test_delete_only_element_in_ll(ll_with_node)
```

<a id="python_solutions.tests.test_LinkedList.test_delete_i_th_element_in_ll_works"></a>

#### test\_delete\_i\_th\_element\_in\_ll\_works

```python
def test_delete_i_th_element_in_ll_works(ll_for_erase)
```

<a id="python_solutions.tests.test_LinkedList.test_neg_indexes_in_erase_in_ll_work"></a>

#### test\_neg\_indexes\_in\_erase\_in\_ll\_work

```python
def test_neg_indexes_in_erase_in_ll_work(ll_for_erase)
```

<a id="python_solutions.tests.test_LinkedList.test_update"></a>

#### test\_update

```python
def test_update(ll_for_erase)
```

<a id="python_solutions.tests.test_LinkedList.test_neg_index_in_update_never_works"></a>

#### test\_neg\_index\_in\_update\_never\_works

```python
def test_neg_index_in_update_never_works(ll_for_erase)
```

<a id="python_solutions.tests.test_LinkedList.test_ll_stores_nones"></a>

#### test\_ll\_stores\_nones

```python
def test_ll_stores_nones(ll_for_erase)
```

<a id="python_solutions.tests.test_LinkedList.test_ll_contains"></a>

#### test\_ll\_contains

```python
def test_ll_contains(ll_for_erase)
```

<a id="python_solutions.tests.test_LinkedList.test_ll_repr"></a>

#### test\_ll\_repr

```python
def test_ll_repr(ll_for_erase)
```

<a id="python_solutions.tests.test_LinkedList.test_indexing_with_neg_numbers_inside_insert"></a>

#### test\_indexing\_with\_neg\_numbers\_inside\_insert

```python
def test_indexing_with_neg_numbers_inside_insert(ll_for_erase)
```

<a id="python_solutions.tests.test_merge_sort.patch"></a>

## patch

<a id="python_solutions.tests.test_merge_sort.test_import_error_for_merge"></a>

#### test\_import\_error\_for\_merge

```python
def test_import_error_for_merge()
```

<a id="python_solutions.tests.test_merge_sort.test_merge_sort_easy_merge"></a>

#### test\_merge\_sort\_easy\_merge

```python
def test_merge_sort_easy_merge()
```

<a id="python_solutions.tests.test_Node.Node"></a>

## Node

<a id="python_solutions.tests.test_Node.pytest"></a>

## pytest

<a id="python_solutions.tests.test_Node.test_can_create_blank_node"></a>

#### test\_can\_create\_blank\_node

```python
def test_can_create_blank_node()
```

<a id="python_solutions.tests.test_Node.node"></a>

#### node

```python
@pytest.fixture()
def node()
```

<a id="python_solutions.tests.test_Node.test_can_assign_data_to_node"></a>

#### test\_can\_assign\_data\_to\_node

```python
def test_can_assign_data_to_node(node)
```

<a id="python_solutions.tests.test_Node.test_can_create_node_with_data"></a>

#### test\_can\_create\_node\_with\_data

```python
def test_can_create_node_with_data()
```

<a id="python_solutions.tests.test_Node.node_with_data"></a>

#### node\_with\_data

```python
@pytest.fixture()
def node_with_data()
```

<a id="python_solutions.tests.test_Node.test_node_can_show_data"></a>

#### test\_node\_can\_show\_data

```python
def test_node_can_show_data(node_with_data)
```

<a id="python_solutions.tests.test_Node.test_node_can_store_next_node"></a>

#### test\_node\_can\_store\_next\_node

```python
def test_node_can_store_next_node(node)
```

<a id="python_solutions.tests.test_Node.test_raises_error_when_next_node_is_not_node_or_none"></a>

#### test\_raises\_error\_when\_next\_node\_is\_not\_node\_or\_none

```python
def test_raises_error_when_next_node_is_not_node_or_none(node)
```

<a id="python_solutions.tests.test_Node.test_raises_error_when_initialized_with_wrong_next_node"></a>

#### test\_raises\_error\_when\_initialized\_with\_wrong\_next\_node

```python
def test_raises_error_when_initialized_with_wrong_next_node()
```

<a id="python_solutions.tests.test_Node.test_eq_for_node"></a>

#### test\_eq\_for\_node

```python
def test_eq_for_node(node_with_data)
```

<a id="python_solutions.tests.test_Node.test_repr_in_node"></a>

#### test\_repr\_in\_node

```python
def test_repr_in_node(node_with_data)
```

<a id="python_solutions.tests.test_Queue.Queue"></a>

## Queue

<a id="python_solutions.tests.test_Queue.pytest"></a>

## pytest

<a id="python_solutions.tests.test_Queue.test_can_make_queue"></a>

#### test\_can\_make\_queue

```python
def test_can_make_queue()
```

<a id="python_solutions.tests.test_Queue.q"></a>

#### q

```python
@pytest.fixture()
def q()
```

<a id="python_solutions.tests.test_Queue.test_can_push_into_queue"></a>

#### test\_can\_push\_into\_queue

```python
def test_can_push_into_queue(q)
```

<a id="python_solutions.tests.test_Queue.test_front_in_queue_works"></a>

#### test\_front\_in\_queue\_works

```python
def test_front_in_queue_works(q)
```

<a id="python_solutions.tests.test_Queue.q_with_4_elements"></a>

#### q\_with\_4\_elements

```python
@pytest.fixture()
def q_with_4_elements()
```

<a id="python_solutions.tests.test_Queue.test_can_pop_from_queue"></a>

#### test\_can\_pop\_from\_queue

```python
def test_can_pop_from_queue(q_with_4_elements)
```

<a id="python_solutions.tests.test_Queue.test_pop_until_one_element_left"></a>

#### test\_pop\_until\_one\_element\_left

```python
def test_pop_until_one_element_left(q_with_4_elements)
```

<a id="python_solutions.tests.test_Queue.test_pop_last_element"></a>

#### test\_pop\_last\_element

```python
def test_pop_last_element(q)
```

<a id="python_solutions.tests.test_real_bin_search.pytest"></a>

## pytest

<a id="python_solutions.tests.test_real_bin_search.real_bin_search"></a>

## real\_bin\_search

<a id="python_solutions.tests.test_real_bin_search.test_real_bin_search_desc"></a>

#### test\_real\_bin\_search\_desc

```python
def test_real_bin_search_desc()
```

<a id="python_solutions.tests.test_real_bin_search.test_real_bin_search_asc"></a>

#### test\_real\_bin\_search\_asc

```python
def test_real_bin_search_asc()
```

<a id="python_solutions.tests.test_real_bin_search.test_search_with_check"></a>

#### test\_search\_with\_check

```python
def test_search_with_check()
```

<a id="python_solutions.tests.test_real_bin_search.test_search_raises_error_when_result_behind_edges_when_check_enabled"></a>

#### test\_search\_raises\_error\_when\_result\_behind\_edges\_when\_check\_enabled

```python
def test_search_raises_error_when_result_behind_edges_when_check_enabled()
```

<a id="python_solutions.tests.test_red_black_tree.pytest"></a>

## pytest

<a id="python_solutions.tests.test_red_black_tree.random"></a>

## random

<a id="python_solutions.tests.test_red_black_tree.math"></a>

## math

<a id="python_solutions.tests.test_red_black_tree.RedBlackTree"></a>

## RedBlackTree

<a id="python_solutions.tests.test_red_black_tree.TreeNode"></a>

## TreeNode

<a id="python_solutions.tests.test_red_black_tree.rb_tree"></a>

#### rb\_tree

```python
@pytest.fixture
def rb_tree()
```

<a id="python_solutions.tests.test_red_black_tree.test_insert"></a>

#### test\_insert

```python
def test_insert(rb_tree)
```

<a id="python_solutions.tests.test_red_black_tree.test_rotations"></a>

#### test\_rotations

```python
def test_rotations()
```

<a id="python_solutions.tests.test_red_black_tree.test_delete"></a>

#### test\_delete

```python
def test_delete(rb_tree)
```

<a id="python_solutions.tests.test_red_black_tree.test_delete_with_error"></a>

#### test\_delete\_with\_error

```python
def test_delete_with_error(rb_tree)
```

<a id="python_solutions.tests.test_red_black_tree.test_search"></a>

#### test\_search

```python
def test_search(rb_tree)
```

<a id="python_solutions.tests.test_red_black_tree.test_random_length_and_elts"></a>

#### test\_random\_length\_and\_elts

```python
def test_random_length_and_elts()
```

<a id="python_solutions.tests.test_segment_tree.pytest"></a>

## pytest

<a id="python_solutions.tests.test_segment_tree.random"></a>

## random

<a id="python_solutions.tests.test_segment_tree.gcd"></a>

## gcd

<a id="python_solutions.tests.test_segment_tree.SegmentTree"></a>

## SegmentTree

<a id="python_solutions.tests.test_segment_tree.SegmentTreeOptimized"></a>

## SegmentTreeOptimized

<a id="python_solutions.tests.test_segment_tree.data1"></a>

#### data1

<a id="python_solutions.tests.test_segment_tree.data2"></a>

#### data2

<a id="python_solutions.tests.test_segment_tree.data"></a>

#### data

<a id="python_solutions.tests.test_segment_tree.test_build_tree"></a>

#### test\_build\_tree

```python
@pytest.mark.parametrize('data', data)
def test_build_tree(data)
```

<a id="python_solutions.tests.test_segment_tree.test_query_sum"></a>

#### test\_query\_sum

```python
@pytest.mark.parametrize('data', data)
def test_query_sum(data)
```

<a id="python_solutions.tests.test_segment_tree.test_query_min"></a>

#### test\_query\_min

```python
@pytest.mark.parametrize('data', data)
def test_query_min(data)
```

<a id="python_solutions.tests.test_segment_tree.test_query_max"></a>

#### test\_query\_max

```python
@pytest.mark.parametrize('data', data)
def test_query_max(data)
```

<a id="python_solutions.tests.test_segment_tree.test_query_gcd"></a>

#### test\_query\_gcd

```python
@pytest.mark.parametrize('data', data)
def test_query_gcd(data)
```

<a id="python_solutions.tests.test_segment_tree.test_update"></a>

#### test\_update

```python
@pytest.mark.parametrize('data', data)
def test_update(data)
```

<a id="python_solutions.tests.test_segment_tree.test_new_action"></a>

#### test\_new\_action

```python
@pytest.mark.parametrize('data', data)
def test_new_action(data)
```

<a id="python_solutions.tests.test_segment_tree.test_build_new_action"></a>

#### test\_build\_new\_action

```python
@pytest.mark.parametrize('data', data)
def test_build_new_action(data)
```

<a id="python_solutions.tests.test_sorts_and_searches.math"></a>

## math

<a id="python_solutions.tests.test_sorts_and_searches.logging"></a>

## logging

<a id="python_solutions.tests.test_sorts_and_searches.pytest"></a>

## pytest

<a id="python_solutions.tests.test_sorts_and_searches.random"></a>

## random

<a id="python_solutions.tests.test_sorts_and_searches.Matrix2dim"></a>

## Matrix2dim

<a id="python_solutions.tests.test_sorts_and_searches.array_count_sort"></a>

## array\_count\_sort

<a id="python_solutions.tests.test_sorts_and_searches.count_sort"></a>

## count\_sort

<a id="python_solutions.tests.test_sorts_and_searches.insert_sort"></a>

## insert\_sort

<a id="python_solutions.tests.test_sorts_and_searches.insert_sort_opt"></a>

## insert\_sort\_opt

<a id="python_solutions.tests.test_sorts_and_searches.merge_sort"></a>

## merge\_sort

<a id="python_solutions.tests.test_sorts_and_searches.merge_sort_parallel"></a>

## merge\_sort\_parallel

<a id="python_solutions.tests.test_sorts_and_searches.quick_sort"></a>

## quick\_sort

<a id="python_solutions.tests.test_sorts_and_searches.digit_sort"></a>

## digit\_sort

<a id="python_solutions.tests.test_sorts_and_searches.digit_sort_opt"></a>

## digit\_sort\_opt

<a id="python_solutions.tests.test_sorts_and_searches.two_dim_array_count_sort"></a>

## two\_dim\_array\_count\_sort

<a id="python_solutions.tests.test_sorts_and_searches.bin_search"></a>

## bin\_search

<a id="python_solutions.tests.test_sorts_and_searches.real_bin_search"></a>

## real\_bin\_search

<a id="python_solutions.tests.test_sorts_and_searches.tern_search_max"></a>

## tern\_search\_max

<a id="python_solutions.tests.test_sorts_and_searches.tern_search_min"></a>

## tern\_search\_min

<a id="python_solutions.tests.test_sorts_and_searches.lower_bound"></a>

## lower\_bound

<a id="python_solutions.tests.test_sorts_and_searches.upper_bound"></a>

## upper\_bound

<a id="python_solutions.tests.test_sorts_and_searches.split_find"></a>

## split\_find

<a id="python_solutions.tests.test_sorts_and_searches.random_1_dim_array"></a>

#### random\_1\_dim\_array

```python
def random_1_dim_array(elts_range=(-100, 100),
                       size_of_1_dim_range=(100, 1000))
```

<a id="python_solutions.tests.test_sorts_and_searches.whole_1_dim_array"></a>

#### whole\_1\_dim\_array

```python
def whole_1_dim_array(elts_range=(-100, 100), size_of_1_dim_range=(100, 1000))
```

<a id="python_solutions.tests.test_sorts_and_searches.whole_2_dim_array"></a>

#### whole\_2\_dim\_array

```python
def whole_2_dim_array(elts_range=(-10, 10),
                      size_of_1_dim_range=(1, 10),
                      size_of_2_dim_range=(10, 100))
```

<a id="python_solutions.tests.test_sorts_and_searches.test_size_range"></a>

#### test\_size\_range

<a id="python_solutions.tests.test_sorts_and_searches.num_range"></a>

#### num\_range

<a id="python_solutions.tests.test_sorts_and_searches.test_sorts"></a>

#### test\_sorts

```python
@pytest.mark.parametrize('function, array, params, sorted_params', [
    (array_count_sort,
     whole_2_dim_array(elts_range=num_range,
                       size_of_1_dim_range=test_size_range,
                       size_of_2_dim_range=test_size_range), {}, {
                           'key': lambda a: a[0]
                       }),
    (insert_sort,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=test_size_range), {}, {}),
    (insert_sort_opt,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=test_size_range), {}, {}),
    (merge_sort,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=test_size_range), {
                            'opt': False
                        }, {}),
    (merge_sort,
     random_1_dim_array(elts_range=num_range, size_of_1_dim_range=(1, 1)), {
         'opt': False
     }, {}),
    (merge_sort_parallel,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=(32, 100)), {}, {}),
    (merge_sort_parallel, [0], {}, {}),
    (merge_sort,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=(101, 1000)), {}, {}),
    (merge_sort,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=(10, 60)), {}, {}),
    (quick_sort,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=test_size_range), {}, {}),
    (quick_sort,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=test_size_range), {
                            'no_recursion': True
                        }, {}),
    (quick_sort,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=test_size_range), {
                            'pivot_str': 'clst_avg',
                            'no_recursion': True
                        }, {}),
    (quick_sort,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=test_size_range), {
                            'pivot_str': 'm3',
                            'no_recursion': True
                        }, {}), (quick_sort, [0], {}, {}),
    (quick_sort,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=test_size_range), {
                            'pivot_str': 'clst_avg'
                        }, {}),
    (quick_sort,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=test_size_range), {
                            'pivot_str': 'm3'
                        }, {}),
    (quick_sort, [1000] + random_1_dim_array(
        elts_range=num_range, size_of_1_dim_range=test_size_range) + [-1000], {
            'pivot_str': 'm3'
        }, {}),
    (quick_sort,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=test_size_range), {
                            'pivot_str': 'mm'
                        }, {}), (quick_sort, [], {}, {}),
    (two_dim_array_count_sort,
     whole_2_dim_array(elts_range=num_range,
                       size_of_1_dim_range=test_size_range,
                       size_of_2_dim_range=test_size_range), {}, {}),
    (two_dim_array_count_sort,
     whole_2_dim_array(elts_range=num_range,
                       size_of_1_dim_range=test_size_range,
                       size_of_2_dim_range=test_size_range), {
                           'keys': [0, 1, 2]
                       }, {
                           'key': lambda x: (x[0], x[1], x[2])
                       }),
    (two_dim_array_count_sort,
     whole_2_dim_array(elts_range=num_range,
                       size_of_1_dim_range=test_size_range,
                       size_of_2_dim_range=test_size_range), {
                           'keys': 2
                       }, {
                           'key': lambda x: x[2]
                       }),
    (count_sort,
     whole_1_dim_array(elts_range=num_range,
                       size_of_1_dim_range=test_size_range), {}, {}),
    (digit_sort,
     whole_1_dim_array(elts_range=num_range,
                       size_of_1_dim_range=test_size_range), {
                           'base': 16
                       }, {}),
    (digit_sort_opt,
     whole_1_dim_array(elts_range=num_range,
                       size_of_1_dim_range=test_size_range), {
                           'base': 16
                       }, {})
])
def test_sorts(function, array, params, sorted_params)
```

<a id="python_solutions.tests.test_sorts_and_searches.test_errors_in_sorts"></a>

#### test\_errors\_in\_sorts

```python
@pytest.mark.parametrize(
    'function, array, params',
    [(two_dim_array_count_sort,
      whole_2_dim_array(elts_range=num_range,
                        size_of_1_dim_range=test_size_range,
                        size_of_2_dim_range=test_size_range), {
                            'keys': ''
                        }),
     (quick_sort,
      random_1_dim_array(elts_range=num_range,
                         size_of_1_dim_range=test_size_range), {
                             'pivot_str': 'mm',
                             'no_recursion': True
                         }),
     (quick_sort,
      random_1_dim_array(elts_range=num_range,
                         size_of_1_dim_range=test_size_range), {
                             'pivot_str': 'cool'
                         })])
def test_errors_in_sorts(function, array, params)
```

<a id="python_solutions.tests.test_sorts_and_searches.test_bin_search"></a>

#### test\_bin\_search

```python
@pytest.mark.parametrize('array', [
    random_1_dim_array(elts_range=num_range,
                       size_of_1_dim_range=test_size_range),
    random_1_dim_array(elts_range=num_range,
                       size_of_1_dim_range=test_size_range),
])
def test_bin_search(array)
```

<a id="python_solutions.tests.test_sorts_and_searches.func"></a>

#### func

```python
def func(x)
```

<a id="python_solutions.tests.test_sorts_and_searches.test_real_bin_search"></a>

#### test\_real\_bin\_search

```python
def test_real_bin_search()
```

<a id="python_solutions.tests.test_sorts_and_searches.test_min_max_tern_search"></a>

#### test\_min\_max\_tern\_search

```python
def test_min_max_tern_search()
```

<a id="python_solutions.tests.test_sorts_and_searches.test_bounds"></a>

#### test\_bounds

```python
@pytest.mark.parametrize('array', [
    whole_1_dim_array(size_of_1_dim_range=(1000, 2000)),
    whole_1_dim_array(size_of_1_dim_range=(100, 2000))
])
def test_bounds(array)
```

<a id="python_solutions.tests.test_sorts_and_searches.test_split_search"></a>

#### test\_split\_search

```python
@pytest.mark.parametrize('array', [
    whole_1_dim_array(elts_range=(-10, 10)),
    whole_1_dim_array(elts_range=(-10, 10))
])
def test_split_search(array)
```

<a id="python_solutions.tests.test_sparse_table.pytest"></a>

## pytest

<a id="python_solutions.tests.test_sparse_table.SparseTable"></a>

## SparseTable

<a id="python_solutions.tests.test_sparse_table.sample_data"></a>

#### sample\_data

<a id="python_solutions.tests.test_sparse_table.sparse_table_instance"></a>

#### sparse\_table\_instance

```python
@pytest.fixture
def sparse_table_instance()
```

<a id="python_solutions.tests.test_sparse_table.test_query_min"></a>

#### test\_query\_min

```python
def test_query_min(sparse_table_instance)
```

<a id="python_solutions.tests.test_sparse_table.test_query_max"></a>

#### test\_query\_max

```python
def test_query_max(sparse_table_instance)
```

<a id="python_solutions.tests.test_sparse_table.test_query_sum"></a>

#### test\_query\_sum

```python
def test_query_sum(sparse_table_instance)
```

<a id="python_solutions.tests.test_sparse_table.test_append_and_extend_raise_errors"></a>

#### test\_append\_and\_extend\_raise\_errors

```python
def test_append_and_extend_raise_errors(sparse_table_instance)
```

<a id="python_solutions.tests.test_Stack.Stack"></a>

## Stack

<a id="python_solutions.tests.test_Stack.pytest"></a>

## pytest

<a id="python_solutions.tests.test_Stack.test_can_make_stack"></a>

#### test\_can\_make\_stack

```python
def test_can_make_stack()
```

<a id="python_solutions.tests.test_Stack.st"></a>

#### st

```python
@pytest.fixture()
def st()
```

<a id="python_solutions.tests.test_Stack.test_can_push_to_stack"></a>

#### test\_can\_push\_to\_stack

```python
def test_can_push_to_stack(st)
```

<a id="python_solutions.tests.test_Stack.test_can_access_stack_back"></a>

#### test\_can\_access\_stack\_back

```python
def test_can_access_stack_back(st)
```

<a id="python_solutions.tests.test_Stack.test_can_access_stack_front"></a>

#### test\_can\_access\_stack\_front

```python
def test_can_access_stack_front(st)
```

<a id="python_solutions.tests.test_Stack.st_with_3_elements"></a>

#### st\_with\_3\_elements

```python
@pytest.fixture()
def st_with_3_elements()
```

<a id="python_solutions.tests.test_Stack.test_can_pop_from_stack"></a>

#### test\_can\_pop\_from\_stack

```python
def test_can_pop_from_stack(st_with_3_elements)
```

<a id="python_solutions.tests.test_Stack.test_pop_until_one_element_left"></a>

#### test\_pop\_until\_one\_element\_left

```python
def test_pop_until_one_element_left(st_with_3_elements)
```

<a id="python_solutions.tests.test_Stack.test_pop_last_element"></a>

#### test\_pop\_last\_element

```python
def test_pop_last_element(st_with_3_elements)
```

<a id="python_solutions.tests.test_Stack.test_can_not_pop_when_zero_elements"></a>

#### test\_can\_not\_pop\_when\_zero\_elements

```python
def test_can_not_pop_when_zero_elements(st)
```

<a id="python_solutions.tests.test_Stack.test_can_not_pop_when_less_than_zero_elements"></a>

#### test\_can\_not\_pop\_when\_less\_than\_zero\_elements

```python
def test_can_not_pop_when_less_than_zero_elements(st)
```

<a id="python_solutions.tests.test_vector.pytest"></a>

## pytest

<a id="python_solutions.tests.test_vector.vector"></a>

## vector

<a id="python_solutions.tests.test_vector.test_can_create_vector_and_len_exists"></a>

#### test\_can\_create\_vector\_and\_len\_exists

```python
def test_can_create_vector_and_len_exists()
```

<a id="python_solutions.tests.test_vector.test_set_and_get_item"></a>

#### test\_set\_and\_get\_item

```python
def test_set_and_get_item()
```

<a id="python_solutions.tests.test_vector.test_insertion"></a>

#### test\_insertion

```python
def test_insertion()
```

<a id="python_solutions.tests.test_vector.test_erase"></a>

#### test\_erase

```python
def test_erase()
```

<a id="python_solutions.tests.test_vector.test_vector_with_cap_lt_size"></a>

#### test\_vector\_with\_cap\_lt\_size

```python
def test_vector_with_cap_lt_size()
```

<a id="python_solutions.tests.test_vector.test_cap_lt_0"></a>

#### test\_cap\_lt\_0

```python
def test_cap_lt_0()
```

<a id="python_solutions.tests.test_vector.test_size_lt_0"></a>

#### test\_size\_lt\_0

```python
def test_size_lt_0()
```

<a id="python_solutions.tests.test_vector.test_vector_pop"></a>

#### test\_vector\_pop

```python
def test_vector_pop()
```

<a id="python_solutions.tests.test_vector.test_empty_vector_extend"></a>

#### test\_empty\_vector\_extend

```python
def test_empty_vector_extend()
```

<a id="python_solutions.tests.test_vector.test_vector_extend"></a>

#### test\_vector\_extend

```python
def test_vector_extend()
```

<a id="python_solutions.tests.test_vector.test_vector_iter"></a>

#### test\_vector\_iter

```python
def test_vector_iter()
```

tests
-----

This module contains unit tests for the algorithms
and data structures implemented in the 'python_solutions' module.

Contents
--------
- Tests for helper-functions for sorts
  - test_array_count_sort.py
  - test_digit_sort.py
  - test_speed_analysis.py
- Tests for helper-functions for searches
  - test_bin_search.py
  - test_real_bin_search.py
- Tests for structures
  - test_bloom_filter.py
  - test_CyclicLinkedList.py
  - test_Deque.py
  - test_DoubleNode.py
  - test_hashtable.py
  - test_heap.py
  - test_LinkedList.py
  - test_Node.py
  - test_Queue.py
  - test_Stack.py
  - test_vector.py
- Tests for performance measurements
  - test_sorts_and_searches.py

Two-Dimensional Array Count Sort Module

This module provides a function, `two_dim_array_count_sort`, for sorting a
2-dimensional array consisting of whole numbers. The function can sort the
1-dimensional arrays inside a 2-dimensional array in ascending order by all
indexes (by default) or by exact indexes in the order they are presented.

Functions
---------
two_dim_array_count_sort(a: list[list[int]], keys: str | list | int = 'all')
    Sorts a 2-dimensional array consisting of whole numbers.

<a id="python_solutions.two_dim_array_count_sort.array_count_sort"></a>

## array\_count\_sort

<a id="python_solutions.two_dim_array_count_sort.two_dim_array_count_sort"></a>

#### two\_dim\_array\_count\_sort

```python
def two_dim_array_count_sort(
- **a**: list[list[int]],

- **keys**: str | list[int] | int = 'all') -> list[list[int]]

```

Sorts a 2-dimensional array consisting of whole numbers.

This function sorts the 1-dimensional arrays inside a 2-dimensional array
in ascending order by all indexes (by default) or by exact indexes
in the order they are presented. Be mindful that this sort populates
an array with absent places in each row's key position with sentinel
values (-inf). In this case the ascending sort will always lead to rows
with absent values being put higher than ones without them.

## Parameters
- **a**: list[list[int]]

    The 2-dimensional array to be sorted.

- **keys**: 'all', list of int, or int, optional

    Specifies the indexes to sort by. If 'all', it sorts by all indexes
    (default). If a list of integers is provided, it sorts by the exact
    indexes in the specified order. If an integer is provided,
    it sorts by a single index.

## Returns

list[list[int]]
    The sorted 2-dimensional array.

## Raises

TypeError
    Raised if the 'keys' argument is of an unsupported type.