from typing import List

"""
Let M be the number of cells in the grid.

Time complexity : O(M). We perform two steps; transposing the matrix, and then reversing
 each row. Transposing the matrix has a cost of O(M) because we're moving
  the value of each cell once.
   Reversing each row also has a cost of O(M),
    because again we're moving the value of each cell once.

Space complexity : O(1) because we do not use any other additional data structures."""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
