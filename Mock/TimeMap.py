from typing import List


class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Set is O(1)
        node = (timestamp, value)
        if key in self.map:
            self.map[key].append(node)
        else:
            self.map[key] = [node]

    def binary_search_iterative(self, array: List[tuple[int, str]], timestamp):
        start = 0
        end = len(array) - 1

        max_str = ""
        max_time = 0

        while start <= end:
            mid = (start + end) // 2
            prev_time = array[mid][0]

            # We found the target
            if timestamp == prev_time:
                return array[mid][1]

            if timestamp < prev_time:
                end = mid - 1
            else:
                start = mid + 1

            if max_time < prev_time <= timestamp:
                max_time = prev_time
                max_str = array[mid][1]

        return max_str

    def get(self, key: str, timestamp: int) -> str:
        # Get is O(Log(N))
        if key in self.map:
            nodes = self.map[key]
            return self.binary_search_iterative(nodes, timestamp)

        else:
            return ""

# Space is O(N)
# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo", "love", 1)
obj.set("foo", "hi", 2)
obj.set("foo", "hi2", 3)
obj.set("foo", "er", 4)
param_2 = obj.get("foo", 2)
print(param_2)
