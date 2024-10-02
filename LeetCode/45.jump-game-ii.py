#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # Initialize variables
        n = len(nums)
        if n == 1:
            return 0
        
        max_reach, steps, jump_end = 0, 0, 0
        
        # Iterate through the array
        for i in range(n - 1):  # No need to check the last element
            max_reach = max(max_reach, i + nums[i])
            
            # When we reach the end of the current jump range
            if i == jump_end:
                steps += 1
                jump_end = max_reach
            
            # If we can already reach or exceed the last index, break early
            if jump_end >= n - 1:
                break
        
        return steps

        
# @lc code=end

