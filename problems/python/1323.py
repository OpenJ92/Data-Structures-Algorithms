class Solution:
    def maximum69Number (self, num: int) -> int:
        def get_digits(num):
            digits = deque()
            while num:
                digit, num = num % 10, num // 10
                digits.append(digit)
            return digits

        digits = get_digits(num)
        power  = len(digits) - 1
        first  = True
        number = 0
        while digits:
            digit = digits.pop()
            if digit == 6 and first:
                digit = 9
                first = False
            number += digit * (10**power)
            power -= 1

        return number
