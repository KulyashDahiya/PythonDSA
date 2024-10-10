#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        cur_sum = 0
        min_len = float('inf')

        for right in range(n):
            cur_sum += nums[right]
            
            while cur_sum >= target:
                min_len = min(min_len, right-left + 1)
                cur_sum -= nums[left]
                left += 1
                

        return min_len if min_len != float('inf') else 0


        
# @lc code=end

