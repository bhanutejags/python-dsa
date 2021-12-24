from typing import List


def binary_search() -> int:
    pass


def imperative_binary_search(input_list: List[int], element_to_search: int) -> int:
    """
    Performs a binary search on the `input_list` to find the `element_to_search`,
    returns its index if found, else returns -1.

    Calculate average temperature from multiple measurements

    >>> imperative_binary_search([10, 11, 13, 34, 91, 101, 137], 127)
    -1

    >>> imperative_binary_search([10, 11, 13, 34, 91, 127, 138], 127)
    5

    :param input_list: The list on which binary search is to be performed.
    :param element_to_search: Element to search for
    :return: Index of the element if found, otherwise -1.
    """
    high = len(input_list)
    low = 0
    mid = (high + low) // 2

    while high - low > 1:
        if input_list[mid] == element_to_search:
            return mid

        if element_to_search < input_list[mid]:
            high = mid
            mid = (high + low) // 2
        elif element_to_search > input_list[mid]:
            low = mid
            mid = (high + low) // 2
    else:
        if input_list[low] == element_to_search:
            return low
        else:
            return -1


def recursive_binary_search(input_list: List[int], element_to_search: int) -> int:
    """
    Performs a binary search on the `input_list` to find the `element_to_search`,
    returns its index if found, else returns -1.

    Calculate average temperature from multiple measurements

    >>> imperative_binary_search([10, 11, 13, 34, 91, 101, 137], 127)
    -1

    >>> imperative_binary_search([10, 11, 13, 34, 91, 127, 138], 127)
    5

    :param input_list: The list on which binary search is to be performed.
    :param element_to_search: Element to search for
    :return: Index of the element if found, otherwise -1.
    """

    def _binary_search(low: int, high: int) -> int:
        nonlocal element_to_search
        nonlocal input_list
        if low == high:
            if input_list[low] == element_to_search:
                return low
            else:
                return -1
        else:
            mid = (low + high) // 2
            if element_to_search == input_list[mid]:
                return mid
            if element_to_search < input_list[mid]:
                return _binary_search(low, mid - 1)
            else:
                return _binary_search(mid + 1, high)

    return _binary_search(0, len(input_list))
