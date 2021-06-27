import pytest

from homework1.task5.task5 import find_maximal_subarray_sum


@pytest.mark.parametrize("list,k,expected_result",
                         [[[1, 3, 45, 66, 7, 8, 8, 8], 4, 126],
                          [[1, 3, 45, 645, 745, 845, 8, 8], 3, 2235],
                          [[1, 23, -45, 65, -745, 845, 8, 8], 2, 853],
                          [[10, 230, -45, 645, -745, 85, 18, 8], 3, 830],
                          ])
def test_find_maximal_subarray_sum(list, k, expected_result):
    assert find_maximal_subarray_sum(list, k) == expected_result
