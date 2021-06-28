import pytest

from Homework1.task1.task1 import check_power_of_2


@pytest.mark.parametrize(
    "value,expected_result",
    [
        (128, True),
        (342, False),
        (1, True),
        (0, False),
    ],
)
def test_power_of_2(value: int, expected_result: bool):
    assert check_power_of_2(value) == expected_result
