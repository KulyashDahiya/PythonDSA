#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        length = 0
        current = head
        while current:
            current = current.next
            length += 1
        
        part_length = length // k
        longer_parts = length % k

        parts = []
        current = head
        for i in range(k):
            parts.append(current)

            part_size = part_length + (1 if i < longer_parts else 0)

            for j in range(part_size - 1):
                if current:
                    current = current.next
                    
            if current:
                next_part_head = current.next
                current.next = None
                current = next_part_head    
        
        
        return parts

        
        
# @lc code=end

