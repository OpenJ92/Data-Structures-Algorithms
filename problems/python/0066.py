class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits) - 1

        for index in range(length, -1, -1):
            if digits[index] == 9:
                digits[index] = 0
            else:
                digits[index] += 1
                return digits

        return [1, *digits]
