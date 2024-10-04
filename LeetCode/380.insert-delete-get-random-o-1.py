#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random
class RandomizedSet:

    def __init__(self):
        self.lis = []
        self.dic = {}
        self.lis_length = 0
        

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False

        self.dic[val] = self.lis_length
        self.lis.append(val)
        self.lis_length += 1

        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

        if val not in self.dic:
            return False

        idx = self.dic[val]
        las_el = self.lis[self.lis_length - 1]

        self.lis[idx] = las_el
        self.dic[las_el] = idx

        self.lis.pop()
        del self.dic[val]

        self.lis_length -= 1

        return True

        

    def getRandom(self) -> int:
        return random.choice(self.lis)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
