# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack, node = [], head
        while node:
            stack.append(node)
            node = node.next

        carry = 0
        while stack:
            node = stack.pop()
            carry, number = divmod(carry + 2 * node.val, 10)
            node.val = number

        if not carry:
            return head
        return ListNode(carry, head)
