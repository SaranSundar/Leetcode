from typing import List
from collections import deque


def markIsland(queue, visited, grid) -> tuple[int, int]:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    time = 0
    oranges_killed = 0
    while queue:
        nodeT = queue.popleft()
        node = nodeT[0]
        distance = nodeT[1]
        for direction in directions:
            newNode = (node[0] + direction[0], node[1] + direction[1])
            if newNode not in visited:
                if 0 <= newNode[1] < len(grid) and 0 <= newNode[0] < len(grid[newNode[1]]):
                    if grid[newNode[1]][newNode[0]] == 1:
                        grid[node[1]][node[0]] = 2
                        oranges_killed += 1
                        visited.add(newNode)
                        queue.append((newNode, distance + 1))

        time = max(time, distance)

    return time, oranges_killed


def orangesRotting(self, grid: List[List[int]]) -> int:
    maxOranges = 0
    stack = []
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 2:
                stack.append((c, r))
            elif grid[r][c] == 1:
                maxOranges += 1

    if maxOranges == 0:
        return 0

    queue = deque([])
    visited = set()

    for s in stack:
        queue.append(((s[0], s[1]), 0))
        visited.add((s[0], s[1]))

    time, oranges_killed = markIsland(queue, visited, grid)
    maxOranges -= oranges_killed

    if maxOranges > 0:
        return -1

    return time


print(orangesRotting(None, [[1, 0, 2, 2, 2]]))
