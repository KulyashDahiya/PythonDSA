#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def check_height(root):

            if not root:
                return 0

            lh = check_height(root.left)
            if lh == -1:
                return -1

            rh = check_height(root.right)
            if rh == -1:
                return -1

            if abs(lh - rh) > 1:
                return -1

            return 1 + max(lh, rh)

        return check_height(root) != -1

            
        
        
# @lc code=end

