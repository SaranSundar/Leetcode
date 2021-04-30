from typing import List


# def canShip(trucks, items):
#     return canShipHelp(trucks, items, 0)
#
# def canShipHelp(trucks, items, index):
#     if all(truck == 0 for truck in trucks):
#         return True
#
#     if index == len(items):
#         return False
#
#     for i in range(len(trucks)):
#         if trucks[i] >= items[index]:
#             trucks[i] -= items[index]
#             result = canShipHelp(trucks, items, index + 1)
#             if result:
#                 return True
#             trucks[i] += items[index]
#
#     return canShipHelp(trucks, items, index + 1)

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

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        self.helper(stones, 0)

    def helper(self, stones: List[int], index: int):
        if len(stones) == 1:
            return True

        if len(stones) == 2:
            if stones[0] == stones[1]:
                return False

        for i in range(index, len(stones)):
            stone1 = stones[i]
            stone2 = stones[index]
            newStone = 0
            if stone1 < stone2:
                newStone = stone2 - stone1
            elif stone1 > stone2:
                newStone = stone1 - stone2
            newStones = [newStone]
            for s in range(len(stones)):
                if s != i and s != index:
                    newStones.append(s)
            return self.helper(newStones, index + 1)

        return True
