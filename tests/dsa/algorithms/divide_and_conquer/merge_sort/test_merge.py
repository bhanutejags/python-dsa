from typing import List

import pytest

from dsa.algorithms.divide_and_conquer.merge_sort import merge


@pytest.mark.parametrize(
    "input_list1,input_list2,expected_merged_list",
    [
        ([0, 2, 4, 6], [0, 3, 6, 9], [0, 0, 2, 3, 4, 6, 6, 9]),
        ([1, 2, 4, 7], [0, 3, 6, 8, 9, 10], [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]),
    ],
)
def test_merge(
    input_list1: List[int], input_list2: List[int], expected_merged_list: List[int]
):
    assert merge(input_list1, input_list2) == expected_merged_list
