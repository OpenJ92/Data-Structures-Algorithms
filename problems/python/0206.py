# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(original, new):
            if not original:
                return new
            return reverse(original.next, ListNode(original.val, new))

        return reverse(head, None)

