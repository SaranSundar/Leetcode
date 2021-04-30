from typing import List


def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    for i in range(len(s) // 2):
        end = len(s) - i - 1
        s[i], s[end] = s[end], s[i]

    print(s)


def reverseStringR(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    for i in range(len(s) // 2):
        end = len(s) - i - 1
        s[i], s[end] = s[end], s[i]

    print(s)


reverseString(None, ["h", "e", "l", "l", "o"])
