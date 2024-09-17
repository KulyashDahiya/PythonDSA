#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Amazon Microsoft Apple Bloomberg Facebook

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev = None
        curr = head

        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt


        return prev
        
# @lc code=end

