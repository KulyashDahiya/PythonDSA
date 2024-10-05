#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0
        elif n == 1:
            return 1

        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i-1] + 1
            
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)

# This problem can be solved in two passes using a greedy approach:

# First, ensure that every child with a higher rating than the child on the left gets more candy than the left child.
# Then, ensure that every child with a higher rating than the child on the right gets more candy than the right child.

        
# @lc code=end

