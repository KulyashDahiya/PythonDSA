#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # lis = s.strip().split(" ")
        # return len(lis[len(lis) - 1])

        end = len(s) - 1

        while end >= 0 and s[end] == " ":
            end -= 1

        start = end
        while start >= 0 and s[start] != " ":
            start -= 1
        
        # return len(s[start + 1 : end + 1])

        return end - start    
# @lc code=end

