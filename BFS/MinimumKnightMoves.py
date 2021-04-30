import heapq
from collections import deque


def get_knight_neighbors(cell):
    directions = [(1, 2), (-1, 2), (2, 1), (-2, 1), (1, -2), (-1, -2), (2, -1), (-2, -1)]
    neighbors = []
    for direction in directions:
        neighbors.append((cell[0] + direction[0], cell[1] + direction[1]))

    return neighbors


def minKnightMoves(self, x: int, y: int) -> int:
    queue = deque([(0, (0, 0))])
    visited = set()
    while queue:
        cell = queue.popleft()
        if cell[1] == (x, y):
            return cell[0]
        neighbors = get_knight_neighbors(cell[1])
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((cell[0] + 1, neighbor))
    return -1


print(minKnightMoves(None, 5, 5))
