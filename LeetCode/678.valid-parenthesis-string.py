#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        def is_valid_with_star_as_open():
            balance = 0
            for char in s:
                if char == '(' or char == '*':
                    balance += 1
                else:  # char == ')'
                    balance -= 1
                if balance < 0:
                    return False
            return True
        
        # Check if the string is valid with '*' treated as ')'
        def is_valid_with_star_as_close():
            balance = 0
            for char in reversed(s):
                if char == ')' or char == '*':
                    balance += 1
                else:  # char == '('
                    balance -= 1
                if balance < 0:
                    return False
            return True
        
        return is_valid_with_star_as_open() and is_valid_with_star_as_close()



# Best Approach -  O(n)

# https://www.youtube.com/watch?v=cHT6sG_hUZI

# def checkValidString(s: str) -> bool:
#     min_open = 0
#     max_open = 0

#     for char in s:
#         if char == '(':
#             min_open += 1
#             max_open += 1
#         elif char == ')':
#             min_open -= 1
#             max_open -= 1
#         else:  # char == '*'
#             min_open -= 1
#             max_open += 1
        
#         # min_open should not go below 0
#         if min_open < 0:
#             min_open = 0

#         # If max_open becomes negative, it means we have more ')' than we can balance
#         if max_open < 0:
#             return False

#     # min_open should be zero for a balanced string
#     return min_open == 0



        
# @lc code=end

