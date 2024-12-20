#
# @lc app=leetcode id=2215 lang=python3
#
# [2215] Find the Difference of Two Arrays
#

# @lc code=start
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        nums1 = set(nums1)
        nums2 = set(nums2)
        return [list(nums1-nums2), list(nums2-nums1)]

        
# @lc code=end

