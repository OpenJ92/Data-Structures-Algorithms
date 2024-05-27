class Solution:
    def specialArray(self, numbers: List[int]) -> int:
        def binary(array, target):
            left, right = 0, len(array)
            while left < right:
                middle = left + ((right - left) // 2)
                if array[middle] >= target:
                    right = middle
                else:
                    left = middle + 1
            return left

        left, right = 0, max(numbers)
        length, _ = len(numbers), numbers.sort()
        while left <= right:
            middle = left + ((right - left) // 2)
            post = length - binary(numbers, middle)
            if post == middle:
                return middle
            elif post < middle:
                right = middle - 1
            else:
                left = middle + 1
        return -1

