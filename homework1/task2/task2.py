from typing import List


def check_fibonacci(Sequence: List[int]) -> bool:
    """
    Сhecking if a sequence of numbers is a fibonacci sequence
    Args:
        Sequence:

    Returns:True or False
    example:
    if sequence=[0,1,1,2,3] then return True

    """

    def fibonacci(n):
        if (n <= 1):
            return n
        else:
            return (fibonacci(n - 1) + fibonacci(n - 2))

    a = []
    for i in range(len(Sequence)):
        a.append(fibonacci(i))
    return Sequence == a  # генерируем последовательность фибоначчи
    # и проверяем равна ли исходной последовательности
