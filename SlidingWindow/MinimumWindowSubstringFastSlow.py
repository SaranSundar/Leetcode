from collections import defaultdict
from typing import List


"""
Time is O(S + P)
Space is O(S + P)
"""




class Solution:
    def minWindow(self, search: str, pattern: str):
        slow = fast = 0
        required = defaultdict(lambda: 0)
        for p in pattern:
            required[p] += 1
        found = defaultdict(lambda: 0)

        requirements_satisfied = 0

        # "ADOBECODEBANC"
        # "Grow ADOBEC"
        # "Shrink DOBEC"
        # "Grow DOBECODEBA"
        # "Shrink ODEBA"
        # "Grow ODEBANC"
        # "Shrink ANC"
        # "Ans= BANC"

        solutions = (-1, len(search) + 1)
        found_length = 0
        while fast < len(search):
            # print("VALUE " + search[slow: fast + 1])
            # Step 1, move right pointer until window has all elements from pattern
            while slow <= fast < len(search):
                if search[fast] in required:
                    found[search[fast]] += 1
                    if found[search[fast]] == required[search[fast]]:
                        requirements_satisfied += 1

                fast += 1

                # Step 2, record desirable window and now shrink slow pointer
                if requirements_satisfied == len(required):
                    # print("GROW " + search[slow: fast + 1])
                    if solutions[1] - solutions[0] > (fast - slow):
                        solutions = (slow, fast)
                    break

            # print("GROW " + search[slow: fast])

            # Step 3, move slow pointer to shrink window
            while slow <= fast:
                if search[slow] in required:
                    found[search[slow]] -= 1
                    if found[search[slow]] < required[search[slow]]:
                        requirements_satisfied -= 1

                slow += 1

                if requirements_satisfied == len(required):
                    # print("Shrink1 " + search[slow: fast + 1])
                    if solutions[1] - solutions[0] > (fast - slow):
                        solutions = (slow, fast)
                else:
                    # print("Shrink2 " + search[slow: fast + 1])
                    break

            # print("SHRINK " + search[slow: fast])
        if solutions == (-1, len(search) + 1):
            return ""
        return search[solutions[0]: solutions[1]]


solution = Solution()
result = solution.minWindow("ADOBECODEBANC", "ABC")
# assert result == "BANC"
print(result)
# result = solution.minWindow("ADOBECODEBANC", "ABC")
# print(result)
