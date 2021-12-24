from __future__ import annotations

from typing import Optional


class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class BinaryTree:
    def __init__(self, root: Node):
        self.root: Node = root
