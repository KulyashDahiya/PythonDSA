#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])
        zero_rows = set()
        zero_columns = set()


        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_columns.add(j)

        
        for row in list(zero_rows):
            matrix[row] = [0 for j in range(columns)]

        for column in list(zero_columns):
            for i in range(rows):
                matrix[i][column] = 0


        return matrix
        
# @lc code=end

