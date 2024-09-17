#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0
        max_altitude = 0
        
        for g in gain:
            current_altitude += g
            max_altitude = max(max_altitude, current_altitude)
        
        return max_altitude

        
# @lc code=end

