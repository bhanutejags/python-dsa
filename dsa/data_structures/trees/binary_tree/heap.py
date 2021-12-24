import abc
from typing import List, Optional, Sized, Union


class Heap(abc.ABC, Sized):
    @abc.abstractmethod
    def insert(self, element: int) -> None:
        ...

    @abc.abstractmethod
    def delete(self) -> int:
        ...


class MaxHeap(Heap):
    """
    An implementation of MaxHeap in Python.
    Internally uses an array to represent the Heap.
    """

    def __init__(self, input_list: Optional[List[int]] = None) -> None:
        if input_list is None:
            input_list = []
        self._tree: List[int] = input_list

    @property
    def tree(self) -> List[int]:
        return self._tree

    def insert(self, element: int) -> None:
        """
        Insert a node as the left-most node in the lowest level.
        """
        # Insert element at the end of the array
        self._tree.append(element)

        element_index = len(self._tree) - 1

        parent_element_index = element_index // 2

        # Move up the new element up the binary _tree,
        # until its value is no longer greater than its parent nodes
        while self._tree[element_index] > self._tree[parent_element_index]:
            parent_element = self._tree[parent_element_index]
            self._tree[parent_element_index] = self._tree[element_index]
            self._tree[element_index] = parent_element

            element_index = parent_element_index
            parent_element_index = element_index // 2

    def delete(self) -> int:
        """
        Delete the Root Node of the MaxHeap.
        """
        deleted_element: int = self._tree.pop(0)
        # Move the last element in the array, or the right-most element
        # on the last line of the Binary Tree,to the root position
        self._tree.insert(0, self._tree.pop(-1))

        element_index = 0

        child_element_indices: tuple[
            Optional[int], Optional[int]
        ] = self._get_child_indices(element_index)

        # Move down the new root element down the binary _tree,
        # until its value is no longer less than its child nodes
        while (
            (child_element_indices[0] is not None)
            and (self._tree[child_element_indices[0]] > self._tree[element_index])
        ) or (
            (child_element_indices[1] is not None)
            and (self._tree[child_element_indices[1]] > self._tree[element_index])
        ):
            if child_element_indices[0] is None:
                break
            elif child_element_indices[1] is None:
                # This the last element in the lowest level
                child_element: int = self._tree[child_element_indices[0]]
                self._tree[child_element_indices[0]] = self._tree[element_index]
                self._tree[element_index] = child_element
                break
            else:
                child_elements = [
                    self._tree[child_element_index]
                    for child_element_index in child_element_indices
                ]

                if child_elements[0] > child_elements[1]:
                    self._tree[child_element_indices[0]] = self._tree[element_index]
                    self._tree[element_index] = child_elements[0]

                    element_index = child_element_indices[0]
                else:
                    self._tree[child_element_indices[1]] = self._tree[element_index]
                    self._tree[element_index] = child_elements[1]

                    element_index = child_element_indices[1]

            child_element_indices = self._get_child_indices(element_index)

        return deleted_element

    def _get_child_indices(
        self, element_index: int
    ) -> Union[tuple[int, int], tuple[int, None], tuple[None, None]]:
        left_child_node_index = (element_index * 2) + 1
        right_child_node_index = (element_index * 2) + 2

        if (left_child_node_index < len(self._tree)) and (
            right_child_node_index < len(self._tree)
        ):
            return left_child_node_index, right_child_node_index
        elif left_child_node_index < len(self._tree):
            return left_child_node_index, None
        else:
            return None, None

    @staticmethod
    def heapify(items_to_insert: List[int]):
        raise NotImplementedError()

    def __len__(self) -> int:
        return len(self._tree)

    def __iter__(self) -> List[int]:
        return self.tree
