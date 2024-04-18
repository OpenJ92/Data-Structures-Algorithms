class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left, right = 0, 1

        while True:
            if reader.get(right) == 2**31 - 1:
                break
            right *= 2

        while left <= right:
            pivot = left + ((right - left) // 2)
            if reader.get(pivot) == target:
                return pivot
            elif reader.get(pivot) < target:
                left = pivot + 1
            else:
                right = pivot - 1

        return -1
