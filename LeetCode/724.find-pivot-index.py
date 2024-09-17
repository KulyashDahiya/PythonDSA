#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            right = total - left - nums[i]
            if right == left:
                return i
            left+=nums[i]
        return -1

        
# @lc code=end

