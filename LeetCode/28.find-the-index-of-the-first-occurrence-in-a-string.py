#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        if haystack == needle or m == 0:
            return 0
        if m > n:
            return -1

        i, j = 0, 0
        while i < n:
            if haystack[i: i + m] == needle:
                return i

            i += 1

        return -1   
# @lc code=end

