from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:

        for r in range(len(board)):
            for c in range(len(board[r])):
                """"
                    Any live cell with fewer than two live neighbors dies as if caused by under-population.
                    Any live cell with two or three live neighbors lives on to the next generation.
                    Any live cell with more than three live neighbors dies, as if by over-population.
                    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                """
                directions = [(1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)]
                live_neighbors = 0
                for direction in directions:
                    new_cell = (direction[0] + r, direction[1] + c)
                    if 0 <= new_cell[0] < len(board) and 0 <= new_cell[1] < len(board[new_cell[0]]):
                        if board[new_cell[0]][new_cell[1]] == 1:
                            live_neighbors += 1

                if 0 <= live_neighbors < 2:
                    board[r][c] = 6
                elif 2 <= live_neighbors <= 3:
                    board[r][c] = 7
                elif live_neighbors > 3:
                    board[r][c] = 8
                elif live_neighbors == 3:
                    board[r][c] = 9
