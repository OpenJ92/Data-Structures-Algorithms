class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        left = 0
        right = len(num) - 1

        strobogrammatic = {
            '0' : '0',
            '1' : '1',
            '6' : '9',
            '8' : '8',
            '9' : '6'
        }

        while left <= right:

            if num[left] in strobogrammatic:
                if strobogrammatic[num[left]] != num[right]:
                    return False
            else:
                return False

            left  += 1
            right -= 1

        return True

