class Solution:
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



