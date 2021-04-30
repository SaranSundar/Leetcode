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

def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    combinations = []
    backtrack(target, [], 0, combinations, candidates)
    return combinations


def backtrack(remain, comb, index, results, candidates):
    # We found solution if remaining is 0
    if remain == 0:
        results.append(list(comb))
        return
    elif remain < 0:
        # No solution possible return false
        return False

    # Loop over values, we will go from index to len of candidates
    for i in range(index, len(candidates)):
        comb.append(candidates[i])
        backtrack(remain - candidates[i], comb, i, results, candidates)
        comb.pop()
