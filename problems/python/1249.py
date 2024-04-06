class Solution:
    def minRemoveToMakeValid(self, string: str) -> str:
        length, stack = len(string), []
        open, closed = '(', ')'

        for index, character in enumerate(string):
            if stack and character == closed and stack[-1][1] == open:
                stack.pop()
                continue

            if character == open or character == closed:
                stack.append((index, character))

        strjng, indices = [], set([index for index, _ in stack])
        for index, character in enumerate(string):
            if index not in indices:
                strjng.append(character)

        return "".join(strjng)
