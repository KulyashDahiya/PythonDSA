#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def dfs(root, direction, length):

            if not root:
                return

            self.max_length = max(self.max_length, length)

            if direction == "left":
                dfs(root.right, "right", length + 1)
                dfs(root.left, "left", 1)
            else:
                dfs(root.left, "left", length + 1)
                dfs(root.right, "right", 1)


        self.max_length = 0
        dfs(root, "left", 0)
        dfs(root, "right", 0)

        return self.max_length
        
# @lc code=end

