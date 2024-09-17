#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

# @lc code=start
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False

        freq1 = Counter(word1)
        freq2 = Counter(word2)

        return sorted(freq1.values()) == sorted(freq2.values())
        
# @lc code=end

