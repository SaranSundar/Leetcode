from typing import List


def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    map = {}
    for i in range(len(arr2)):
        map[arr2[i]] = i

    def custom_key(key):
        if key in map:
            return map[key]
        else:
            return (len(arr2)) + key

    # Returns the ordering
    arr1.sort(key=custom_key)

    return arr1

arr1 = relativeSortArray(None, [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6])
print(arr1)
