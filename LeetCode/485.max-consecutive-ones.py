#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        ct_count = max_count = 0

        for i in range(len(nums)):

            if nums[i] == 1:
                ct_count += 1
            else:
                ct_count = 0

            max_count = max(ct_count, max_count)

        return max_count
            


                
        
# @lc code=end

