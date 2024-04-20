class Solution:
    def decodeString(self, string: str) -> str:
        stack = []

        for character in string:
            strjng = []
            while stack and stack[-1] != '[' and character == ']':
                strjng.append(stack.pop())

            if strjng and character == ']':
                number, _ = [], stack.pop()
                while stack and stack[-1] in set('1234567890'):
                    number.append(stack.pop())

                _, _ = strjng.reverse(), number.reverse()
                strkng, number = "".join(strjng), "".join(number)

                stack.append(int(number) * strkng)

            if character != ']':
                stack.append(character)

        return ''.join(stack)
