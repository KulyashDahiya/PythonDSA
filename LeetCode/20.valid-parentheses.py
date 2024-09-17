#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = { ")": "(", "}": "{", "]": "["}

        for char in s:
            if char in char_map.values():
                stack.append(char)
            else:
                if not stack or stack.pop() != char_map[char]:
                    return False
                
        return not stack
        
# @lc code=end

