# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sentinal = ListNode()
        curr = sentinal
        heap = []

        for k in range(len(lists)):
            if lists[k]:
                heappush(heap, (lists[k].val, k, lists[k]))

        while heap:
            _, k, node = heappop(heap)
            curr.next = node
            curr = curr.next
            node = node.next

            if node:
                heappush(heap, (node.val, k, node))

        return sentinal.next
