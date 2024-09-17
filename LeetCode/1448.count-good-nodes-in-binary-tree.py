#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0
            
            # Count this node as good if its value is >= max_val
            good = 1 if node.val >= max_val else 0
            
            # Update max_val for the path
            max_val = max(max_val, node.val)
            
            # Recursively count good nodes in left and right subtrees
            good += dfs(node.left, max_val)
            good += dfs(node.right, max_val)
            
            return good

        # Start DFS with a very small initial max value
        return dfs(root, float('-inf'))
# @lc code=end

