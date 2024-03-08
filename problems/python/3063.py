# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = Counter()

        while head:
            counter[head.val] += 1
            head = head.next
        
        sentinel = ListNode()
        sentjnel = sentinel
        for (_, freq) in sorted(counter.items()):
            sentinel.next = ListNode(freq)
            sentinel = sentinel.next
        
        return sentjnel.next
