# mypy: ignore-errors
from typing import List


def quick_sort(input_list: List[int]) -> List[int]:
    def _partition(low: int, high: int) -> int:
        pivot: int = input_list[low]
        i: int = low
        j: int = high

        while i < j:
            while input_list[i] < pivot:
                i += 1

            while input_list[j] > pivot:
                j -= 1

            if i < j:
                # swap elements at i and j indices
                input_list[i], input_list[j] = input_list[j], input_list[i]

        input_list[low], input_list[j] = input_list[j], input_list[low]
        return j

    def _quick_sort(low: int, high: int):
        if low < high:
            j = _partition(low, high)
            _quick_sort(low, j)
            _quick_sort(j + 1, high)
        else:
            pass

    return []
