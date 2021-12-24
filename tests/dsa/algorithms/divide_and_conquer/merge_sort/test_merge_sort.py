import hypothesis.strategies as st
import pytest
from hypothesis import given

from dsa.algorithms.divide_and_conquer.merge_sort import (
    merge_sort_recursive,
    two_way_merge_sort,
)


@pytest.mark.parametrize(
    "input_list,expected_sorted_list",
    [
        ([8, 4, 11, 3, 10, 12, 32, 47], [3, 4, 8, 10, 11, 12, 32, 47]),
        ([7, 4, 11, 3, 10, 12, 21, 47], [3, 4, 7, 10, 11, 12, 21, 47]),
        # ([12, 7, 22, 11, 1, 10, 13], [1, 7, 10, 11, 12, 13, 22]),
    ],
)
def test_merge_sort(input_list, expected_sorted_list):
    assert two_way_merge_sort(input_list) == expected_sorted_list


@pytest.mark.parametrize(
    "input_list,expected_sorted_list",
    [
        ([8, 4, 11, 3, 10, 12, 32, 47], [3, 4, 8, 10, 11, 12, 32, 47]),
        ([12, 7, 22, 11, 1, 10, 13], [1, 7, 10, 11, 12, 13, 22]),
    ],
)
def test_merge_sort_recursive(input_list, expected_sorted_list):
    assert merge_sort_recursive(input_list) == expected_sorted_list


@given(st.lists(st.integers()))
def test_merge_sort_recursive_sum_property(input_list):
    assert sum(merge_sort_recursive(input_list)) == sum(input_list)


def is_identical(list_a, list_b):
    if len(list_a) != len(list_b):
        return False
    for i in list_a:
        if i not in list_b:
            return False
    return True


@given(st.lists(st.integers()))
def test_merge_sort_recursive_same_elements_property(input_list):
    assert is_identical(merge_sort_recursive(input_list), input_list)
