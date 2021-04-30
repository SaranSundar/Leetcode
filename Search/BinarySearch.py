from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            # Add the high and low to get the real middle number
            middle = (high + low) // 2

            if nums[middle] == target:
                return middle

            if nums[middle] < target:
                low = middle + 1
            elif nums[middle] > target:
                high = middle - 1

        return -1
