from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    if board[r][c] == word or self.helper_dfs(board, r, c, word):
                        return True

        return False

    def helper_dfs(self, board: List[List[str]], r: int, c: int, word: str) -> bool:
        stack = [(0, (r, c))]
        visited = {(r, c)}
        while stack:
            index, cell = stack.pop()

            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for direction in directions:
                new_cell = (direction[0] + cell[0], direction[1] + cell[1])
                if 0 <= new_cell[0] < len(board) and 0 <= new_cell[1] < len(board[new_cell[0]]):
                    if new_cell not in visited:
                        if index == len(word) - 1:
                            return True

                        if index + 1 < len(word):
                            if board[new_cell[0]][new_cell[1]] == word[index + 1]:
                                visited.add(new_cell)
                                stack.append((index + 1, new_cell))
                        else:
                            return False

        return False


solution = Solution()
print(solution.exist([["a", "b", "c"],
                      ["a", "e", "d"],
                      ["a", "f", "g"]], "abcdefg"))
