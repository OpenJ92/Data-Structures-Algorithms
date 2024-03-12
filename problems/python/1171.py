class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def values(head):
            values = []
            while head:
                if head.val != 0:
                    values.append(head.val)
                head = head.next
            return values

        def make(stack):
            output = ListNode()
            sentinel = output
            for value, _ in stack:
                sentinel.next = ListNode(value)
                sentinel = sentinel.next
            return output.next

        stack    = []
        totals   = set([0])
        elements = values(head)
        for element_next in elements:
            if not stack:
                stack.append((element_next, element_next))
                totals.add(element_next)
                continue

            total_next = stack[-1][1] + element_next
            if total_next not in totals:
                totals.add(total_next)
                stack.append((element_next, total_next))
                continue

            while stack and not stack[-1][1] == total_next:
                _, total = stack.pop()
                totals.remove(total)

        return make(stack)
