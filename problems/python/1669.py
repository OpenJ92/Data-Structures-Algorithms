# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list_one: ListNode, lower: int, upper: int, list_two: ListNode) -> ListNode:
        sentinel_one = ListNode(next = list_one)
        sentinel_two = list_one
        difference = upper - lower

        while sentinel_one.next and lower:
            sentinel_one = sentinel_one.next
            sentinel_two = sentinel_two.next
            lower -= 1

        sentinel_one.next = list_two

        sentjnel_one = list_two
        while sentjnel_one.next:
            sentjnel_one = sentjnel_one.next

        while sentinel_two.next and difference:
            sentinel_two = sentinel_two.next
            difference -= 1

        sentjnel_one.next = sentinel_two.next

        return list_one


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list_one: ListNode, lower: int, upper: int, list_two: ListNode) -> ListNode:
        sentinel_one = ListNode(next = list_one)
        sentinel_two = list_one
        difference = upper - lower

        while sentinel_two.next and lower:
            sentinel_one = sentinel_one.next
            sentinel_two = sentinel_two.next
            lower -= 1
        sentinel_one.next = list_two

        while list_two.next:
            list_two = list_two.next

        while sentinel_two.next and difference:
            sentinel_two = sentinel_two.next
            difference -= 1
        list_two.next = sentinel_two.next

        return list_one
