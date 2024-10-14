#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        result = []  
        
        # Define the boundaries for the matrix traversal
        top, bottom = 0, len(matrix) - 1        # Top and bottom boundaries (row indices)
        left, right = 0, len(matrix[0]) - 1     # Left and right boundaries (column indices)
        
        # Continue looping until all boundaries are crossed
        while top <= bottom and left <= right:
            
            # Traverse from left to right along the top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            # Move the top boundary down, since the top row is processed
            top += 1
            
            # Traverse down the right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            # Move the right boundary left, since the right column is processed
            right -= 1
            
            # Check if there are any rows left to traverse from right to left (bottom row)
            if top <= bottom:
                # Traverse from right to left along the bottom row
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                # Move the bottom boundary up, since the bottom row is processed
                bottom -= 1
            
            # Check if there are any columns left to traverse from bottom to top (left column)
            if left <= right:
                # Traverse up the left column
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                # Move the left boundary right, since the left column is processed
                left += 1

        # Return the result list which contains the matrix elements in spiral order
        return result
        
# @lc code=end

