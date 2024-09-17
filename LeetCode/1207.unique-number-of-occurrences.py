#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = dict(Counter(arr))
        print(dic)
        seen_freq = set()
        for value in dic.values():
            if value in seen_freq:
                return False
            seen_freq.add(value)

        return True
        
# @lc code=end

