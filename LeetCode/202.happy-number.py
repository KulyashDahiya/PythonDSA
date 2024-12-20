#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:

        def next_num(n):
            total_sum = 0
            while n:
                digit = n % 10
                total_sum += digit ** 2
                n //= 10
                            
            return total_sum
        
        nums = set()
        
        while n != 1:
            nums.add(n)
            n = next_num(n)

            if n in nums:
                return False
        
        return True


        # def next_num(n):
        #     total_sum = 0
        #     while n:
        #         digit = n % 10
        #         total_sum += digit ** 2
        #         n //= 10
                            
        #     return total_sum

        # slow = n
        # fast = next_num(n)

        # while fast != 1 and slow != fast:
        #     slow = next_num(slow)
        #     fast = next_num(next_num(fast))

        # return fast == 1
        
# @lc code=end

