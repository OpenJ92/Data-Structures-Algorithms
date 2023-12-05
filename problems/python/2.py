# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        number = ListNode(); pointer = number
        while l1 and l2:
          digit = ((l1.val + l2.val + carry) % 10)
          carry = ((l1.val + l2.val + carry) // 10)
          pointer.val = digit
          l1 = l1.next
          l2 = l2.next
          if l1 or l2:
            pointer.next = ListNode()
            pointer = pointer.next

        while l1:
          digit = (l1.val + carry) % 10
          carry = (l1.val + carry) // 10
          pointer.val = digit
          if l1.next:
            pointer.next = ListNode()
            pointer = pointer.next
          l1 = l1.next

        while l2:
          digit = (l2.val + carry) % 10
          carry = (l2.val + carry) // 10
          pointer.val = digit
          if l2.next:
            pointer.next = ListNode()
            pointer = pointer.next
          l2 = l2.next

        if carry:
          pointer.next = ListNode()
          pointer = pointer.next
          pointer.val = carry

        return number
