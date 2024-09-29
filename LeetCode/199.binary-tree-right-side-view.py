#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def reverse_pre_order(root, level):
            nonlocal ds

            if not root:
                return

            if len(ds) == level:
                ds.append(root.val)

            reverse_pre_order(root.right, level + 1)
            reverse_pre_order(root.left, level + 1)


        ds = []
        reverse_pre_order(root, 0)

        return ds


        # https://www.youtube.com/watch?v=KV4mRzTjlAk
        
# @lc code=end

