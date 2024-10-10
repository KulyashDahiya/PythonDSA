#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)


# Approaxh 1: Using Hash Map for 2 sum
        res = set()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            seen = set()  # Set to track elements for Two-Sum
            for j in range(i + 1, n):
                complement = target - nums[j]
                if complement in seen:
                    res.add((nums[i], nums[j], complement))

                seen.add(nums[j])
        
        return list(res)




# Approach  2: Using two pointers
        # res = []
        # for i in range(n):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue

        #     j = i + 1
        #     k = n - 1

        #     while j < k:
        #         total = nums[i] + nums[j] + nums[k]
        #         if total == 0:
        #             res.append([nums[i], nums[j], nums[k]])
        #             j += 1
        #             k -= 1

        #             while j < k and nums[j] == nums[j-1]:
        #                 j += 1
        #             while j < k and nums[k] == nums[k+1]:
        #                 k -= 1

        #         elif total < 0:
        #             j += 1
        #         else:
        #             k -= 1

        # return res


# BruteForce Approach : O(n^3)
        # res = set()  # To store unique triplets        
        # Iterate through all possible triplets
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 # Sort the triplet before adding to avoid duplicates in different orders
        #                 triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
        #                 res.add(triplet)
        
        # return list(res)

# @lc code=end

