def intToRoman(self, num: int) -> str:
    """
        Time and space complexity O(1)

        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
    """
    roman = ""
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    for i in range(len(values)):
        value = values[i]
        if value > num:
            continue
        repeat = num // value
        num = num % value
        for c in range(repeat):
            roman += symbols[i]

    return roman


assert intToRoman(None, 3) == "III"
assert intToRoman(None, 4) == "IV"
assert intToRoman(None, 9) == "IX"
assert intToRoman(None, 58) == "LVIII"
assert intToRoman(None, 1994) == "MCMXCIV"
