#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0

        while i < len(nums):

            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

            i += 1
        
        return j
        
# @lc code=end

