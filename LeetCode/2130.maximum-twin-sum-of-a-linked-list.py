#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Amazon

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow, fast = head, head
        maxVal = 0

	    # Get middle of linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse second part of linked list
        curr, prev = slow, None
        while curr:       
            curr.next, prev, curr = prev, curr, curr.next  

        # printLL(head)
        # printLL(rev_head)

        while prev:
            maxVal = max(maxVal, head.val + prev.val)
            prev = prev.next
            head = head.next

        return maxVal
        
# @lc code=end

