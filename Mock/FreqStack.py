from heapq import heappop, heappush


class FreqStack:

    def __init__(self):
        self.pq = []
        self.freq = {}

    def push(self, val: int) -> None:
        frequency = 0
        if val in self.freq:
            frequency = self.freq[val] + 1
            self.freq[val] += 1
        else:
            frequency = 1
            self.freq[val] = 1
        value = (-frequency, -(len(self.pq) + 1), val)
        print(value)
        heappush(self.pq, value)

    def pop(self) -> int:
        value = heappop(self.pq)
        print(value)
        return value[2]


# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
obj.push(9)
obj.push(3)
obj.push(4)
obj.push(2)
obj.push(6)
obj.push(1)
obj.pop()
obj.push(4)
obj.pop()

print("---------")
for i in range(4):
    obj.pop()
