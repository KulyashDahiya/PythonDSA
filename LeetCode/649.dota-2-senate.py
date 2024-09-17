#
# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#

# @lc code=start
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        qr, qd = deque(), deque()

        for i, s in enumerate(senate):
            if s == 'R':
                qr.append(i)
            else:
                qd.append(i)
        
        while qr and qd:
            r, d = qr.popleft(), qd.popleft()

            if r < d:
                qr.append(r+n)
            else:
                qd.append(d+n)

        return "Radiant" if qr else "Dire"
# @lc code=end

