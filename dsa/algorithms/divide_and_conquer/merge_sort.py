from math import log2
from typing import List


def merge(input_list1: List[int], input_list2: List[int]) -> List[int]:
    """
    Performs a merge on the two sorted lists.
    """
    i: int = 0
    j: int = 0
    merged_list: List[int] = []
    while (i < len(input_list1)) and (j < len(input_list2)):
        if input_list1[i] > input_list2[j]:
            merged_list.append(input_list2[j])
            j += 1
        else:
            merged_list.append(input_list1[i])
            i += 1

    # Copy any leftover elements,
    # either input_list1 or input_list2 have leftover elements but not both.
    for e in input_list1[i:]:
        merged_list.append(e)

    for e in input_list2[j:]:
        merged_list.append(e)

    return merged_list


def two_way_merge_sort(input_list: List[int]) -> List[int]:
    number_of_passes: int = int(log2(len(input_list)))

    for this_pass in range(1, number_of_passes + 1):
        sorted_list: List[int] = []
        left_over_items = len(input_list) - (len(input_list) // 2 ** this_pass) * (
            2 ** this_pass
        )

        i = 0
        while i < (len(input_list) - left_over_items):
            shift = 2 ** (this_pass - 1)
            sorted_list += merge(
                input_list[i : i + shift], input_list[i + shift : i + shift + shift]
            )
            i += 2 ** this_pass

        sorted_list += input_list[i:]
        input_list = sorted_list

    return input_list


def merge_sort_recursive(input_list: List[int]) -> List[int]:
    def _recursive_merge_sort(low: int, high: int) -> List[int]:
        if high > low:
            mid = (low + high) // 2
            return merge(
                _recursive_merge_sort(low, mid), _recursive_merge_sort(mid + 1, high)
            )
        else:
            return input_list[low : low + 1]

    return _recursive_merge_sort(0, len(input_list))
