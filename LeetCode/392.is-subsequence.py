#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        if t == '' and s != '':
            return False

        j = 0
        n = len(t)
        m = len(s)

        for i in range(n):
            if j == m:
                break
            if t[i] == s[j]:
                j += 1


        return True if j== m else False
        
# @lc code=end

