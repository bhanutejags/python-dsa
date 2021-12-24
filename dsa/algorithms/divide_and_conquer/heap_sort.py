# mypy: ignore-errors
from typing import List

from dsa.data_structures.trees.binary_tree.heap import Heap


def heap_sort(heap: Heap) -> List[int]:
    return [heap.delete() for i in range(len(heap))]
