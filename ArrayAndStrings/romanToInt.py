values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}


def romanToInt(self, input_str: str) -> int:
    """
    Time complexity : O(1).

    This is a problem limitation, normally its O(n)
    As there is a finite set of roman numerals, the maximum number possible number can be 3999,
     which in roman numerals is MMMCMXCIX. As such the time complexity is O(1)

    If roman numerals had an arbitrary number of symbols, then the time complexity would be
     proportional to the length of the input,
     i.e. O(n). This is assuming that looking up the value of each symbol is O(1).

    Space complexity : O(1).

    Because only a constant number of single-value variables are used, the space complexity is O(1).
    """
    result = 0
    i = 0
    while i < len(input_str):
        if i + 1 < len(input_str) and input_str[i: i + 2] in values:
            result += values[input_str[i: i + 2]]
            i += 2
        else:
            result += values[input_str[i: i + 1]]
            i += 1

    return result
