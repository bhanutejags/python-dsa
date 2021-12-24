import pytest

from dsa.algorithms.divide_and_conquer.binary_search import recursive_binary_search
from tests.dsa.algorithms.divide_and_conquer.binary_search import test_data


@pytest.mark.parametrize(
    "input_list,element_to_search,expected",
    test_data,
)
def test_recursive_parametrized(input_list, element_to_search, expected):
    assert recursive_binary_search(input_list, element_to_search) == expected
