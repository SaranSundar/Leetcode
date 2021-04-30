"""
Time Complexity: O(N). Here, N is the length of
 string input_str. We perform only one iteration over string input_str.

 Space Complexity: O(1) We use constant extra space for storing sign of the result.
"""


def myAtoi(self, input_str: str) -> int:
    input_str = input_str.strip()
    sign = 1
    start = 0
    num = 0

    if len(input_str) == 0:
        return 0
    elif input_str[0] == '+':
        sign = 1
        start = 1
    elif input_str[0] == '-':
        sign = -1
        start = 1

    while start < len(input_str):
        if '0' <= input_str[start] <= '9':
            num = num * 10 + int(input_str[start])
            if num * sign > 2 ** 31 - 1:
                num = 2 ** 31 - 1
                break
            elif num * sign < - (2 ** 31):
                num = (2 ** 31)
                break
        else:
            break
        start += 1

    return sign * num


assert myAtoi(None, "   -42") == -42
assert myAtoi(None, "42") == 42
assert myAtoi(None, "4193 with words") == 4193
assert myAtoi(None, "words and 987") == 0
assert myAtoi(None, "-91283472332") == -2147483648
