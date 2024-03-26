class Solution:
    def isValid(self, string: str) -> bool:
        if len(string) % 2 == 1:
            return False

        stack = []
        open = set(['{','[','('])
        matching = {')':'(', ']':'[', '}':'{'}

        while string:
            paren, *string = string
            if paren in open:
                stack.append(paren)
                continue

            if stack and matching[paren] == stack[-1]:
                stack.pop()
                continue

            stack.append(paren)
        return not stack

