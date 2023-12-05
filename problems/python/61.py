# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: 
            return head

        left = 0
        right = 0

        ## Get length of linked list
        length = 0
        length_node = head
        while length_node:
            length_node = length_node.next
            length += 1

        ## Adjust k to remve redundant rotations. 
        k = k % length
        if k == 0:
            return head

        sentinal_second = ListNode(next=head)
        second = head
        ## Slide right pointer, sentinal second and 
        ## second node out to k elements out.
        while right < k:
            second = second.next
            sentinal_second = sentinal_second.next
            right += 1

        ## Slide second to end of list with first in tow.
        ## Sentinal Nodes maintained for stitching
        sentinal_first = ListNode(next=head)
        first = head
        while second:
            sentinal_first = sentinal_first.next
            first    = first.next
            sentinal_second = sentinal_second.next
            second   = second.next

        ## rebuild rotated list and return new head.
        sentinal_second.next = head
        sentinal_first.next = None
        return first
