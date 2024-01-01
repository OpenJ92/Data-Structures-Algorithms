class Recursive:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(path, open, closed, parenthesis):
            if not open and not closed:
                parenthesis.append(path[:])

            if open:
                op = open.pop()
                backtrack(path + op, open, closed, parenthesis)
                open.append('(')

            if closed and len(closed) > len(open):
                cl = closed.pop()
                backtrack(path + cl, open, closed, parenthesis)
                closed.append(')')

        parenthesis = []
        open   = ['('] * n
        closed = [')'] * n
        backtrack("", open, closed, parenthesis)
        return parenthesis

class Iterative:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = deque([(n, n, '')])
        out   = deque([])
        while stack:
            open, closed, parenthesis = stack.pop()
            if not open and not closed:
                out.append(parenthesis)
                continue
            if open:
                stack.append((open-1, closed, parenthesis+'('))
            if closed and closed > open:
                stack.append((open, closed-1, parenthesis+')'))
        return out



