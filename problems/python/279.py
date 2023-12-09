class Solution:
    def numSquares(self, n: int) -> int:
        target = n

        def squares(curr):
            squares_list = []
            square = 1
            while square**2 <= curr:
                squares_list.append(square**2)
                square += 1
            squares_list.reverse()
            return squares_list
        
        def valid(next):
            return next >= 0

        queue = deque([(target, 0)])
        state = set([target])
        while queue:
            curr, steps = queue.popleft()
            if curr == 0:
                return steps

            for square in squares(curr):
                next = curr - square
                if valid(next) and next not in state:
                    queue.append((next, steps+1))
                    state.add(next)

        return 0
        
