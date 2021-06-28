import pytest

from Homework1.task4.task4 import check_sum_of_four


@pytest.mark.parametrize(
    "list1,list2,list3,list4,expected_result",
    [
        [[0, 0], [0, 0], [0, 0], [0, 0], 16],
        [[0, 3, 2], [0, 2, -3], [4, 2, 1], [1, 3, -3], 4],
        [[0, 0, 2], [0, 1, -3], [4, -2, 1], [1, 1, -3], 6],
        [[0, 0, 2, 4], [0, 1, -3, 2], [4, -2, 1, -4], [1, 1, -3, -2], 19],
    ],
)
def test_check_sum_of_four(list1, list2, list3, list4, expected_result):
    assert check_sum_of_four(list1, list2, list3, list4) == expected_result
