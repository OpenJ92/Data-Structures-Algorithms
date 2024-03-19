class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        @cache
        def backtrack(length):
            if length > high:
                return 0

            _zero = backtrack(length + zero)
            _one  = backtrack(length + one)

            return (_zero + _one + int(low <= length <= high)) % (10**9 + 7)

        return backtrack(0)

