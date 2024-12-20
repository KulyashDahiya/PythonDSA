#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        num_map = defaultdict()

        for i, num in enumerate(nums):
            
            if num in num_map and abs(i - num_map[num]) <= k:
                return True

            num_map[num] = i
        
        return False
        
# @lc code=end

