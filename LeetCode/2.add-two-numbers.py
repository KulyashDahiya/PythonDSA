#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummyhead = ListNode()
        current = dummyhead
        carry = 0

        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total%10)

            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummyhead.next


        # def listToLL(list):
        #     dummyhead = ListNode()
        #     current = dummyhead
        #     for num in list:
        #         current.next = ListNode(num)
        #         current = current.next
        #     return dummyhead.next
        #
        # def lltoList(node):
        #     result = []
        #     while node:
        #         result.append(node.val)
        #         node = node.next
        #     return result
        #
        # def listToInteger(lst):
        #     s = ""
        #     for num in lst:
        #         s += str(num)
        #
        #     return int(s)
        #
        # def integerToList(num):
        #     s = str(num)
        #     lst = []
        #     for char in s:
        #         lst.append(int(char))
        #     return lst
        #
        # first_number = lltoList(l1)[::-1]
        # second_number = lltoList(l2)[::-1]
        # result_number = listToInteger(first_number) + listToInteger(second_number)
        #
        # result_list = integerToList(result_number)[::-1]
        # print(result_list)
        #
        # result = listToLL(result_list)
        #
        # return result

        
# @lc code=end

