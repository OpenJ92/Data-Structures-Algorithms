# https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if not head:
            return [None] * k

        length = self.get_length(head)
        partition_size = length // k
        remainder = length % k

        partitions = []
        current_node = head

        for _ in range(k):
            partition_length = partition_size + (remainder > 0)

            if current_node:
                partitions.append(current_node)
                for _ in range(partition_length - 1):
                    current_node = current_node.next

                next_node = current_node.next
                current_node.next = None
                current_node = next_node
                remainder -= 1
            else:
                partitions.append(None)

        return partitions

    def get_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
