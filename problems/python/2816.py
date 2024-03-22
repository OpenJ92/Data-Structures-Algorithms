# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def backtrack(node):
            if not node:
                return 0, None

            carry, npde = backtrack(node.next)
            carry, number = divmod(carry + 2 * node.val, 10)
            node.val, node.next = number, npde

            return carry, node

        carry, node = backtrack(head)
        if not carry:
            return node
        return ListNode(carry, node)

class Inplace:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def backtrack(node):
            if not node:
                return 0

            carry = backtrack(node.next)
            carry, number = divmod(carry + 2 * node.val, 10)
            node.val = number

            return carry

        carry = backtrack(head)
        if not carry:
            return head
        return ListNode(carry, head)
