def strStr(self, haystack: str, needle: str) -> int:
    if needle == "" or needle == haystack:
        return 0
    if len(needle) > len(haystack):
        return -1

    i = 0
    while i < len(haystack):
        if i + len(needle) <= len(haystack) and haystack[i: i + len(needle)] == needle:
            return i
        i += 1

    return -1


assert strStr(None, haystack="hello", needle="ll") == 2
assert strStr(None, haystack="aaaaa", needle="bba") == -1
assert strStr(None, haystack="", needle="") == 0
