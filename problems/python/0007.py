class Solution:
    def reverse(self, x: int) -> int:
        elements = []
        parity = 1 if x > 0 else -1
        x = parity * x
        while (True):
            elements = [(x % 10), *elements]
            x = (x - (x % 10)) / 10
            if (x <= 0):
                break

        reversed_x = parity * sum([element*(10**i) for i, element in enumerate(elements)])
        if reversed_x > 2**31 - 1 or reversed_x < -2**31:
            return 0
        else:
            return int(reversed_x)

class Solution:
    def reverse(self, x: int) -> int:
        parity = 1 if x > 0 else -1
        x = parity * x

        digits = []
        while x > 0:
            digits = [(x % 10), *digits]
            x = (x - (x % 10)) // 10

        reversed_x = 0
        for index, digit in enumerate(digits):
            reversed_x += digit*(10**index)
        reversed_x *= parity

        if reversed_x > 2**31 - 1 or reversed_x < - 2**31:
            return 0
        return reversed_x

