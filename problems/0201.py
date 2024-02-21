class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0

        while left != right:
            right >>= 1
            left  >>= 1
            shift += 1

        return left << shift
