#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Optimal Approach : Transpose and Reverse

        n = len(matrix)

        # Transposing
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reversing
        for i in range(n):
            matrix[i] = reversed(matrix[i])

        return matrix


        
# @lc code=end

