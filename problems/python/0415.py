class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        out = []; carry = 0
        while num1 and num2:
            *num1, num = num1
            *num2, ber = num2

            num = int(num)
            ber = int(ber)
            sum = num + ber + carry

            if sum >= 10: carry = 1
            else:         carry = 0

            out = [str(sum % 10), *out]

        while num1:
            *num1, num = num1

            num = int(num)
            sum = num + carry

            if sum >= 10: carry = 1
            else: carry = 0

            out = [str(sum % 10), *out]

        while num2:
            *num2, ber = num2

            ber = int(ber)
            sum = ber + carry

            if sum >= 10: carry = 1
            else: carry = 0

            out = [str(sum % 10), *out]

        if carry: out = ['1', *out]

        return "".join(out)
