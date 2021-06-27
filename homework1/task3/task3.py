from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """
    finding the minimum and maximum number
    Args:
        file_name:

    Returns:typle
    Example:
         if array=[1,2,3,4,5]
         Returns:(1,5)
    """
    with open(file_name) as fi:
        min = int(fi.readline())
        max = min
        for line in fi:
            line = int(line.rstrip('\n'))  # удаление переноса строки
            if min >= line:  # и перевод оставшейся части в число
                min = line
            elif max <= line:
                max = line
    return min, max
