from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        copy = sorted(list(set(arr)))
        map = {}
        for i in range(len(copy)):
            map[copy[i]] = i
        result = []
        for i in arr:
            result.append(map[i] + 1)
        return result
