from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        num_walkable_cells = 0
        start_row = 0
        start_col = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    start_row = r
                    start_col = c
                if 0 <= grid[r][c] <= 2:
                    num_walkable_cells += 1

        visited = {(start_row, start_col)}
        return self.helper(grid, start_row, start_col, visited, num_walkable_cells)

    def helper(self, grid: List[List[int]], row, col, visited: set, num_walkable_cells) -> int:
        if len(visited) == num_walkable_cells and grid[row][col] == 2:
            return 1
        elif grid[row][col] == 2:
            return 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        total_paths = 0
        for direction in directions:
            newCell = (direction[0] + row, direction[1] + col)
            if 0 <= newCell[0] < len(grid) and 0 <= newCell[1] < len(grid[newCell[0]]):
                if newCell not in visited and grid[newCell[0]][newCell[1]] != -1:
                    visited.add(newCell)

                    total_paths += self.helper(grid, newCell[0], newCell[1], visited, num_walkable_cells)

                    visited.remove(newCell)

        return total_paths
