#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

# @lc code=start
from collections import defaultdict
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        max_length = 0
        zero_count = 0
        
        for right in range(len(nums)):

            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            length = right - left
            max_length = max(max_length, length)

        return max_length - 1 if max_length == len(nums) else max_length

            
        
# @lc code=end

