#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    from collections import defaultdict
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_to_dic = defaultdict(int)

        for i, num in enumerate(nums):
            complement = target - num

            if complement in nums_to_dic:
                return [nums_to_dic[complement], i]
            else:
                nums_to_dic[num] = i
        
# @lc code=end

