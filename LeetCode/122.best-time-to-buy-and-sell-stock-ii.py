#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

# For each day i, if the price is higher than the previous day (prices[i] > prices[i-1]), we add the difference (prices[i] - prices[i-1]) to the max_profit.

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        
        return max_profit


# OR

        # if not prices:
        #     return 0

        # min_price = float('inf')
        # profit = 0

        # for price in prices:

        #     if price < min_price:
        #         min_price = price
            
        #     if price - min_price > 0:
        #         profit += price - min_price
        #         min_price = price
            
        # return profit
        
# @lc code=end

