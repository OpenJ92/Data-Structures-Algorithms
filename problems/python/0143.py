class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return head

        def backtrack(one, two, three):
            if two.next.next:
                one = backtrack(one, two.next, three.next)
            if not one or one.next == three or one == three:
                return None

            sentinel = one.next
            one.next = three
            two.next = None
            three.next = sentinel

            return sentinel

        backtrack(head, head, head.next)
