from typing import List

import pytest

from dsa.algorithms.divide_and_conquer.heap_sort import MaxHeap


@pytest.mark.parametrize(
    "elements_to_insert,expected_heap",
    [[[2, 3, 4], [[2], [3, 2], [4, 3, 2]]], [[3, 1, 5], [[3], [3, 1], [5, 3, 1]]]],
)
def test_max_heap_insert(elements_to_insert: List[int], expected_heap):
    max_heap = MaxHeap()
    for index, element in enumerate(elements_to_insert):
        max_heap.insert(element)
        assert max_heap.tree == expected_heap[index]


# @pytest.mark.parametrize("initial_heap,number_of_deletes,expected_heap")
# def test_max_heap_delete(initial_heap: List[int], number_of_deletes, expected_heap):
#     max_heap = MaxHeap.new(initial_heap)
#
#     for i in range(number_of_deletes):
#         max_heap.delete()
#         assert max_heap.tree == expected_heap[i]


@pytest.mark.parametrize(
    "initial_heap,number_of_deletes,expected_heap",
    [
        ([60, 50, 35, 16, 15, 32, 31], 1, [50, 31, 35, 16, 15, 32]),
        ([60, 50, 35, 16, 15, 32, 31], 2, [35, 31, 32, 16, 15]),
    ],
)
def test_max_heap_delete(initial_heap, number_of_deletes, expected_heap):
    max_heap = MaxHeap(initial_heap)

    for _i in range(number_of_deletes):
        max_heap.delete()
    assert max_heap.tree == expected_heap
