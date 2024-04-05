class Solution:
    def makeGood(self, string: str) -> str:
        stack = []

        def valid(first, second):
            return first.islower() and second.isupper() and first.upper() == second

        for character in string:
            if stack and (valid(stack[-1], character) or valid(character, stack[-1])):
                stack.pop()
                continue
            
            stack.append(character)
        
        return "".join(stack)
