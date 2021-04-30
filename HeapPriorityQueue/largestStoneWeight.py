from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for s in stones:
            heapq.heappush(pq, -s)

        while len(pq) >= 2:
            y = -heapq.heappop(pq)
            x = -heapq.heappop(pq)
            z = y - x
            if z != 0:
                heapq.heappush(pq, -z)

        return 0 if len(pq) == 0 else -heapq.heappop(pq)
