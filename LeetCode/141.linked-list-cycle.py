#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import defaultdict

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # dic = defaultdict(int)
        # current = head
        # while current:

        #     if current in dic:
        #         return True

        #     dic[current] += 1
        #     current = current.next

        # return False

        if not head:
            return False

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True


        return False

         
        
# @lc code=end

