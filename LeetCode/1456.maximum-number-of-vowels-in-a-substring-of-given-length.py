#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
        
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        max_vowels = current_count = 0
    
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        max_vowels = current_count

        for i in range(k, len(s)):
            
            if s[i-k] in vowels:
                current_count -= 1
            
            if s[i] in vowels:
                current_count += 1

            max_vowels = max(current_count, max_vowels)

        return max_vowels
            

        
# @lc code=end

