class Solution:
    """
    Time complexity : O(n). Index end will iterate n times.

    Space complexity : O(min(m, n)). We need O(k) space for the sliding window,
    where k is the size of the Set. The size of the Set is upper bounded by the
    size of the string n and the size of the charset/alphabet m.

    """
    def lengthOfLongestSubstring(self, substring: str) -> int:
        ans = 0
        # copy stores the current index of a character
        copy = {}

        slow = 0
        # try to extend the range [slow, fast]
        for fast in range(len(substring)):
            letter = substring[fast]
            if letter in copy:
                slow = max(copy[letter] + 1, slow)

            ans = max(ans, fast - slow + 1)
            copy[letter] = fast

        return ans
