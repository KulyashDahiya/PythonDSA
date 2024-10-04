#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:

        # n = len(citations)

        # if n == 1:
        #     return 1 if citations[0] > 0 else 0

        # citations.sort(reverse=True)

        # for i in range(n):
        #     if citations[i] <= i:
        #         return i
        
        # return n

        n = len(citations)

        if n == 1:
            return 1 if citations[0] > 0 else 0

        citations.sort(reverse = True)

        h_index = 0

        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h_index = i + 1
            else:
                break

        return h_index
        
# @lc code=end

