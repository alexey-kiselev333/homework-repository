from typing import List
from collections import defaultdict


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """
    Checking for the equality to zero of the sum of arrays
    Args:
        a:
        b:
        c:
        d:

    Returns:number
    Examples:
        if a=[0,0]
           b=[0,0]
           c=[0,0]
           d=[0,0]
           Returns:16
    """
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    count_z = 0
    for i in range(len(a)):
        for j in range(len(a)):
            d1[a[i] + b[j]] += 1  # Если нет повторяющегося ключа,то записываем его в словарь
            d2[c[i] + d[j]] += 1  # со значением 1.Если есть,то прибавляем единицу
    for key in d1:
        if -key in d2:
            count_z += d1[key] * d2[-key]
    return count_z
