#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def min_node(root):

            curr = root
            while curr.left:
                curr = curr.left

            return curr.val

        def delete_node(root, key):

            if not root:
                return

            if root.val > key:
                root.left = delete_node(root.left, key)
            elif root.val < key:
                root.right = delete_node(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                elif not root.left and root.right:
                    return None

                min_val = min_node(root.right)

                root.val = min_val
                root.right = delete_node(root.right, min_val)

            return root

        return delete_node(root, key)
        
# @lc code=end

