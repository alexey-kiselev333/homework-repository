import os
from typing import Tuple

import pytest
from homework1.task3.task3 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        (os.path.join("test_textfile1.txt"), (1, 3)),
        (os.path.join("test_textfile2.txt"), (-1, 9)),
        (os.path.join("test_textfile3.txt"), (-6, 6454)),
        (os.path.join("test_textfile4.txt"), (34, 46646)),

    ],
)
def find_maximum_and_minimum(file_name: str, expected_result: Tuple[int, int]):
    assert find_maximum_and_minimum(file_name) == expected_result
