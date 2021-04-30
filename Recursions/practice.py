def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


def factorial2(n):
    temp = 1
    while n >= 1:
        temp *= n
        n -= 1
    return temp


# def canShip(trucks, items):
#     return canShipHelp(trucks, items, 0)
#
# def canShipHelp(trucks, items, index):
#     if all(truck == 0 for truck in trucks):
#         return True
#
#     if index == len(items):
#         return False
#
#     for i in range(len(trucks)):
#         if trucks[i] >= items[index]:
#             trucks[i] -= items[index]
#             result = canShipHelp(trucks, items, index + 1)
#             if result:
#                 return True
#             trucks[i] += items[index]
#
#     return canShipHelp(trucks, items, index + 1)

# def findSolutions(n, other params) :
#     if (found a solution) :
#         displaySolution();
#         return true;
#
#       <Optional>
#      if no solution possible:
#          return false
#
#
#     for (val = first to last) :
#         if (isValid(val, n)) :
#             applyValue(val, n);
#             if (findSolutions(n+1, other params))
#                 return true;
#             removeValue(val, n);
#         return false;


# def generateParenthesis(n):
#     results = []
#     helper(n, n, "", results)
#     return results
#
# def helper(nOpen, nClosed, currString, results):
#     if nOpen == nClosed == 0:
#         results.append(currString)
#     else:
#         for c in ["(", ")"]:
#             if c == "(" and nOpen > 0:
#                 helper(nOpen - 1, nClosed, currString + "(", results)
#             if c == ")" and nClosed > nOpen:
#                 helper(nOpen, nClosed - 1, currString + ")", results)
#
# print(generateParenthesis(3))


# letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
#                "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
#
# def phone_letter(digits):
#     results = list()
#     helper(digits, 0, "", results)
#     return results
#
# def helper(digits, index, currString, results):
#     if index == len(digits):
#         results.append(currString)
#     else:
#         for letter in letters[digits[index]]:
#             helper(digits, index + 1, currString + letter, results)
#
# print(phone_letter("23"))
