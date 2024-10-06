#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:

##  Approach: 2-Pointer Technique

        if not height:
            return 0

        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        total_water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    total_water += max_left - height[left]
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    total_water += max_right - height[right]
                right -= 1

        return total_water
            






## Using Dynamic Programming -- Time Complexity: O(n), Space Complexity: O(n)

        # if not height:
        #     return 0

        # n = len(height)

        # left_max = [0] * n
        # max_left = 0
        # for i in range(n):
        #     left_max[i] = max_left
        #     max_left = max(max_left, height[i])

        # right_max = [0] * n
        # max_right = 0
        # for i in range(n-1, -1, -1):
        #     right_max[i] = max_right
        #     max_right = max(max_right, height[i])
        

        # total_water = 0
        # for i in range(n):
        #     total_water += max(0, min(left_max[i], right_max[i]) - height[i])


        # return total_water
        
# @lc code=end

