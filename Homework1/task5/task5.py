from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if len(nums) < k or k == 0:
        return "Error,pls write correct list"
    maxarray = nums[:k]  # Пусть сумма первых элементов будет максимальной
    for i in range(k, len(nums) + 1):
        if sum(maxarray) < sum(
            nums[i - k : i]
        ):  # Если сумма следующих элементов больше
            maxarray = nums[i - k : i]  # предыдущих, то пусть она будет максимальной
    return sum(maxarray)
