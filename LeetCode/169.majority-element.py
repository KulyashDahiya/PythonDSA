#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dic = defaultdict(int)

        for i in range(len(nums)):
            dic[nums[i]] += 1
            
            if dic[nums[i]] > len(nums)/2:
                return nums[i]


        # counter = Counter(nums)

        # for num, count in counter.items():
        #     print(num, count)
        #     if count > len(nums)/2:
        #         return num

        
# @lc code=end

