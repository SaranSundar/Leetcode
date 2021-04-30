import heapq


def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    pq = []

    # Time is O(N* Log(K))
    # Space is O(K)
    # return heapq.nlargest(k, nums)[-1]

    for n in nums:
        heapq.heappush(pq, n)
        if len(pq) > k:
            heapq.heappop(pq)

    return heapq.heappop(pq)
