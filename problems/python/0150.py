class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {
            '+' : lambda x, y: x + y,
            '-' : lambda x, y: x - y,
            '*' : lambda x, y: x * y,
            '/' : lambda x, y: math.trunc(x / y)
        }
                
        stack = deque()
        for token in tokens:
            if token not in operands:
                stack.append(int(token))
                continue

            y, x = stack.pop(), stack.pop()
            val = operands[token](x, y)
            stack.append(val)
        
        return stack.pop()
