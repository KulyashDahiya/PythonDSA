#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_mirror(l, r):

            if not l and not r:
                return True

            if not l or not r:
                return False

            if l.val == r.val:
                return is_mirror(l.left, r.right) and is_mirror(l.right, r.left)

            return False


        if root:
            return is_mirror(root.left, root.right)

        return True
        
# @lc code=end

