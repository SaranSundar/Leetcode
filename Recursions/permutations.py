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

# def permute(self, nums: List[int]) -> List[List[int]]:
#     permutations = []
#     backtrack(nums, permutations, [], 0)
#     # [1,2,3]
#     # [3, 2, 1]
#     # []
#
#
# def backtrack(nums, permutations, current, index):
#     if len(current) == len(nums):
#         permutations.append(list(current))
#     else:
#         for i in range(index, len(nums)):
#             if nums[i] not in current:
#                 current.append(nums[i])
#                 backtrack(nums, permutations, current, index)
#                 current.pop()
#

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    def backtrack(first=0):
        # if all integers are used up
        if first == n:
            output.append(nums[:])
        for i in range(first, n):
            # place i-th integer first
            # in the current permutation
            nums[first], nums[i] = nums[i], nums[first]
            print(nums)
            # use next integers to complete the permutations
            backtrack(first + 1)
            # backtrack
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    output = []
    backtrack()
    return output


print(permute([1, 2, 3]))
