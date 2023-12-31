# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def eGCD(x, y):
            while(y):
               x, y = y, x % y
            return abs(x)

        left  = head
        right = head.next

        while left and right:
            middle = ListNode(val = eGCD(left.val, right.val))

            left.next = middle
            middle.next = right

            left  = right
            right = right.next

        return head
