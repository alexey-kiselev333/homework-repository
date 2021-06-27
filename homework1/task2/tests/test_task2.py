import pytest
from homework1.task2.task2 import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([0, 1, 1, 2, 3, 5], True),
        ([0, 1, 1], True),
        ([0, 1, 1, 2, 3, 8], False),
        ([0, 1, 1], True),
        ([0, 1, 2], False),
    ],
)
def test_check_fibonacci(value: int, expected_result: bool):
    assert check_fibonacci(value) == expected_result
