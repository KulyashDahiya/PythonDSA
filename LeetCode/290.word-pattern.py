#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lis1 = [i for i in pattern]
        lis2 = s.split(" ")

        if len(lis1) != len(lis2):
            return False

        dic1 = {}
        dic2 = {}

        print(lis1, lis2)
        # print(dic1, dic2)


        for a, b in zip(lis1, lis2):

            if a in dic1:
                if dic1[a] != b:
                    return False
            else:
                dic1[a] = b

            if b in dic2:
                if dic2[b] != a:
                    return False
            else:
                dic2[b] = a

        return True
        
# @lc code=end

