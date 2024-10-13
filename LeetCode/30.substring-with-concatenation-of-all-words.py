#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

 # Sliding Window Approach (Most Opimised) T.C -> O(n), where n is the length of the string s ; S.C -> O(m), where m is the total number of words in the list words.

        n = len(s)
        res = []
        word_len = len(words[0])
        total_words = len(words)
        counter = Counter(words)

        for i in range(word_len):
            left = i
            right = i
            cur_counter = Counter()
            cur_words = 0

            while right + word_len <= n:

                word = s[right: right + word_len]
                right += word_len

                if word in counter:
                    cur_counter[word] += 1
                    cur_words += 1

                    while cur_counter[word] > counter[word]:
                        left_word = s[left:left+word_len]
                        cur_counter[left_word] -= 1
                        left += word_len
                        cur_words -= 1

                    if cur_words == total_words:
                        res.append(left)

                else:
                    left = right
                    cur_counter.clear()
                    cur_words = 0


        return res


 # Sliding Window Approach   (181/182 Test Case Passed 1 Time Limit Exceeded)
        # e_length = len(words[0])
        # f_length = len(words) * e_length
        # res = []

        # for i in range(len(s) - f_length + 1):
        #     counter = Counter(words)
        #     left = i
        #     right = left + e_length

        #     cur_scan = 0

        #     while cur_scan < f_length:

        #         word = s[left:right]

        #         if word in counter and counter[word] > 0:
        #             cur_scan += e_length
        #             counter[word] -= 1
        #             left = right
        #             right = left + e_length 

        #         else:
        #             break


        #     if cur_scan == f_length:
        #         res.append(i)

        # return res


# Brute Force --- TimeOut

        # n = len(words)
        # if n == 1:
        #     return s[0]
        
        # res = []
        
        # concatenations = [''.join(perm) for perm in itertools.permutations(words)]
        # initials = [words[i][0] for i in range(n)]
        # common_length = len(concatenations[0])

        # for i in range(len(s)):
        #     if s[i] in initials and s[i:i+common_length] in concatenations:
        #         res.append(i)

        # return res


        
# @lc code=end

