from typing import List


def missingElement(self, nums: List[int], k: int) -> int:
    # [4, 7, 9, 10] k = 3
    # take the difference between 2 numbers and then minus 1 to get the amount of numbers in between
    diff = 0
    for i in range(1, len(nums)):
        diff += (nums[i] - nums[i - 1]) - 1
        if diff >= k:
            return nums[i - 1] + (diff - k) + (i - 1)

    # Diff is less then k
    return nums[0] + k + (len(nums) - 1)


print(missingElement(None, [1, 2, 4], 3))
