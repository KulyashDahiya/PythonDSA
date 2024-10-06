#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)

        shortest = min(strs, key = len)
        res = ""

        for i in range(len(shortest)):
            flag = True
            curr = strs[0][i]

            for j in range(1, n):
                if strs[j][i] != curr:
                    flag = False

            if flag:
                res += curr
            else:
                break
        
        return res
        
# @lc code=end

