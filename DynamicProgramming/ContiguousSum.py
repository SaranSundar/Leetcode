from typing import List


# def findSolutions(n, other params) :
#     if (found a solution) :
#         displaySolution();
#         return true;
#
#       <Optional>
#      if no solution possible:
#          return false
#
#
#     for (val = first to last) :
#         if (isValid(val, n)) :
#             applyValue(val, n);
#             if (findSolutions(n+1, other params))
#                 return true;
#             removeValue(val, n);
#         return false;

def maxSubArray(self, nums: List[int]) -> int:
    pass


def helper(nums, maxSum, currentSum, current, index, answer):
    if currentSum > maxSum:
        return True
    else:
        if index == len(nums):
            return False

        for i in range(index, len(nums)):
            current.append(nums[i])
            helper(nums, maxSum, currentSum + nums[i], )
