from collections import defaultdict

"""
Time is O(N*K*logK) K is max length of a string in strs
N is length of strs input array

Space is O(N*K) total info stored in ans
"""


class Solution(object):
    def groupAnagrams(self, strs):
        ans = defaultdict(list)
        for s in strs:
            # sorted returns list, list cant be key
            ans[tuple(sorted(s))].append(s)
        return ans.values()
