def firstUniqChar(self, input_str: str) -> int:
    copy = {}
    for s in input_str:
        if s in copy:
            copy[s] = copy[s] + 1
        else:
            copy[s] = 1

    for i in range(len(input_str)):
        if copy[input_str[i]] == 1:
            return i
    return -1