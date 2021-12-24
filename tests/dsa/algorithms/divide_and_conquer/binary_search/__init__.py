import pytest

test_data = [
    pytest.param(list(range(0, 200, 2)), 2, 1, id="test1"),
    pytest.param(list(range(0, 200, 3)), 9, 3, id="test2"),
    pytest.param(list(range(0, 200, 2)), 9, -1, id="test1-non-existent-element"),
    pytest.param(list(range(0, 150, 32)), 42, -1, id="test2-non-existent-element"),
]
