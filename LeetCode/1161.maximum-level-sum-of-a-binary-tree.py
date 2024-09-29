#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        max_sum = float('-inf')
        max_level = 0
        current_level = 1

        q = deque()
        q.append(root)

        while q:
            level_sum = 0
            level_size = len(q)

            for i in range(level_size):

                c = q.popleft()
                level_sum += c.val

                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)

            if level_sum > max_sum:
                max_level = current_level
                max_sum = level_sum

            current_level += 1


        return max_level
        
# @lc code=end

