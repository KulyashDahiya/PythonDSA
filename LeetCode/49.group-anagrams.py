#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = defaultdict(list)
        ans = []

        for word in strs:
            key = ''.join(sorted(word))
            word_dict[key].append(word)
        
        for key, value in word_dict.items():
            ans.append(value)

        return ans


        
# @lc code=end

