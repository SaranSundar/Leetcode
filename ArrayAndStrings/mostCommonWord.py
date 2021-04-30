from typing import List


def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    paragraph = paragraph.strip().lower()
    ignore = "!?',;."
    for i in ignore:
        paragraph = paragraph.replace(i, " ")
    copy = {}
    paragraph = paragraph.split(" ")
    count = 0
    word = ""
    for p in paragraph:
        if p == "" or p == " ":
            continue
        if p not in banned:
            if p in copy:
                copy[p] += 1
            else:
                copy[p] = 1
            if copy[p] > count:
                count = copy[p]
                word = p
    return word


assert mostCommonWord(None, "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]) == "ball"
assert mostCommonWord(None, "a, a, a, a, b,b,b,c, c", ["a"]) == "b"
