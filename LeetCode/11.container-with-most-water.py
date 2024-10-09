#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:

        maxArea = 0
        left = 0
        right = len(height) - 1

        while left < right:

            h = min(height[left], height[right])  
            maxArea = max((right - left) * h, maxArea)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1


        return maxArea


        
# @lc code=end

