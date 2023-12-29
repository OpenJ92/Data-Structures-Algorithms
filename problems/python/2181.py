# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left  = head
        right = head

        acc = 0
        while right.next:
            right = right.next
            acc += right.val

            if right.val == 0:
                node = ListNode(val = acc)
                left.next = node
                node.next = right
                left = right
                acc = 0

        top = head.next
        while top:
            top.next = top.next.next
            top = top.next

        return head.next

