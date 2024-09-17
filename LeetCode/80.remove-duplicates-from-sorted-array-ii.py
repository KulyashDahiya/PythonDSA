#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        j = 2

        for i in range(1, len(nums)):
            if nums[i] != nums[j-2]:
                nums[j] = nums[i]
                j += 1

        return j

        
# @lc code=end
