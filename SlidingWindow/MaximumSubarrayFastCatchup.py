from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = float('-inf')
        fast = 0

        currentTotal = 0
        while fast < len(nums):
            currentTotal += nums[fast]
            fast += 1
            if currentTotal > total:
                total = currentTotal

            if currentTotal <= 0:
                currentTotal = 0

        return total
