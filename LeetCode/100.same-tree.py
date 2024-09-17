#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def levelOrder(root):

            if not root:
                return []

            q = deque([root])
            path = [root.val]

            while q:
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                    path.append(node.left.val)
                else:
                    path.append('null')

                if node.right:
                    q.append(node.right)
                    path.append(node.right.val)
                else:
                    path.append('null')

            return path

        path_p = levelOrder(p)
        path_q = levelOrder(q)

        return path_p == path_q


# Best Approach

# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if not p and not q:
#             return True
#         if not p or not q:
#             return False
#         return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
# @lc code=end

