#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        # lis = s.strip().split()
        # lis.reverse()
        # return " ".join(lis)

    # OR

        # return " ".join(reversed(s.split()))

    # OR

        n = len(s)
        if not s or (n == 1 and s[0] != ' '):
            return s

        ans = ""
        start = end = len(s) - 1
        c = 1

        while start > 0:
            while end >= 0 and s[end] == " ":
                end -= 1

            start = end
            while start >= 0 and s[start] != " ":
                start -= 1
            
            ans += s[start + 1: end + 1] + " "

            end = start
        

        end = len(ans) - 1
        while end >= 0 and ans[end] == " ":
            end -= 1
        
        return ans[:end+1]
# @lc code=end

