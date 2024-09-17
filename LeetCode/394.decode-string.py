#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        current_str = ""
        current_num = 0
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                num_stack.append(current_num)
                current_num = 0
                str_stack.append(current_str)
                current_str = ""               
            elif char == ']':
                prev_str = str_stack.pop()
                prev_num = num_stack.pop()
                current_str = prev_str + (current_str * prev_num)
            else:
                current_str += char
            
        return current_str
        
# @lc code=end

