from typing import List

"""
Time complexity : O(n). Single pass.

Space complexity : O(1). Constant space is used.
"""


def maxArea(self, height: List[int]) -> int:
    start = 0
    area = 0
    end = len(height) - 1

    while start < end:
        current_area = min(height[start], height[end]) * (end - start)
        area = max(area, current_area)
        if height[start] <= height[end]:
            start += 1
        else:
            end -= 1

    return area


assert maxArea(None, [1, 1]) == 1
assert maxArea(None, [4, 3, 2, 1, 4]) == 16
assert maxArea(None, [1, 2, 1]) == 2
assert maxArea(None, [1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
