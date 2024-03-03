class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def backtrack(output, first, mover):
            if mover.next:
                output, first, _ = backtrack(output, first, mover.next)
            return output and (first.val == mover.val), first.next, mover

        output, _, _ = backtrack(True, head, head)
        return output
