#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_leaf_values(self, root: Optional[TreeNode]) -> list:
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        return self.get_leaf_values(root.left) + self.get_leaf_values(root.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        leaves1 = self.get_leaf_values(root1)
        leaves2 = self.get_leaf_values(root2)

        return leaves1 == leaves2


        
# @lc code=end

