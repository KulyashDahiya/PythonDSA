#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(root):
            nonlocal ans
            if not root:
                return

            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)


        ans = []
        dfs(root)
        return ans
        
# @lc code=end

