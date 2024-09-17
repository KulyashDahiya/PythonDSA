#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, current_sum):
            if not root:
                return

            current_sum += root.val

            self.count += prefix_sum.get(current_sum - targetSum, 0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

            dfs(root.left, current_sum)
            dfs(root.right, current_sum)

            prefix_sum[current_sum] -= 1


        self.count = 0
        prefix_sum = {0:1}
        dfs(root, 0)

        return self.count



### Simpler

        # def dfs(root, current_sum):

        #     if not root:
        #         return 0
            
        #     current_sum += root.val

        #     count = prefix_sums.get(current_sum - targetSum, 0)
        #     prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

        #     count += dfs(root.left, current_sum) 
        #     count += dfs(root.right, current_sum)

        #     prefix_sums[current_sum] -= 1

        #     return count


        # prefix_sums = {0: 1}
        # return dfs(root, current_sum=0)
        
# @lc code=end

