class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            match operation:
                case '+':
                    one = stack.pop()
                    two = stack.pop()
                    stack.extend([two, one, one + two])
                case 'D':
                    one = stack.pop()
                    stack.extend([one, 2*one])
                case 'C':
                    stack.pop()
                case _:
                    stack.append(int(operation))
        if not stack: return 0
        return sum(stack)
