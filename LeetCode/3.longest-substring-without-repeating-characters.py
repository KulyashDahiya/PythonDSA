#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    # def is_repeating(self, s: str) -> bool:

    #     seen = set()
    #     for char in s:
    #         if char in seen:
    #             return True
    #         seen.add(char)

    #     return False

    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = set()
        left = 0
        max_len = 0

        
        for right in range(len(s)):
            
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            max_len = max(max_len, right-left + 1)

        return max_len



# Apprach with use of Bool Funciton

        # max_len = 0
        # start = 0
        # running_str = ''

        # for end in range(len(s)):
        #     running_str += s[end]

        #     while self.is_repeating(running_str):
        #         running_str = s[start : end+1]
        #         start += 1
                                    
        #     max_len = max(max_len, len(running_str))

        # return max_len

        
# @lc code=end

