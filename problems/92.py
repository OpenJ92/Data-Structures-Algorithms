# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        sentinal_one = ListNode(0, head)
        prev = sentinal_one
        curr = head
        while left > 1:
            curr = curr.next
            prev = prev.next
            left  -= 1
            right -= 1

        sentinal_two = ListNode(0, curr)
        prev_two = sentinal_two
        while right:
            next = curr.next
            curr.next = prev_two
            prev_two = curr
            curr = next
            right -= 1

        prev.next.next = next
        prev.next = prev_two

        return sentinal_one.next

