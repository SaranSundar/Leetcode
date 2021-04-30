from typing import List

"""
Time complexity : O(n). We traverse the list containing n elements only 
once. Each look up in the table costs only O(1) time.

Space complexity : O(n). The extra space required depends on the number of items stored in the hash table,
 which stores at most n elements.

"""


def twoSum(self, nums: List[int], target: int) -> List[int]:
    copy = {}
    ans = []
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in copy:
            return [copy[complement], i]
        copy[nums[i]] = i
    return ans


def twoSumSorted(self, nums: List[int], target: int) -> List[int]:
    start = 0
    end = len(nums) - 1
    while start < end:
        total = nums[start] + nums[end]
        if total == target:
            return [start + 1, end + 1]
        if total < target:
            start += 1
        else:
            end -= 1


print(twoSum(None, [2, 5, 5, 11], 10))
