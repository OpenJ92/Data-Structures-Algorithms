class Solution:
    def search(self, numbers: List[int], target: int) -> int:

        def ordered(left, right):
            return left <= right and numbers[left] <= numbers[right]

        def between(left, right):
            return left <= right and numbers[left] <= target <= numbers[right]

        def binary_search(array, target, left, right):
            while left <= right:
                pivot = left + ((right - left) // 2)
                if array[pivot] == target:
                    return pivot
                elif array[pivot] > target:
                    right = pivot - 1
                else:
                    left = pivot + 1
            return -1

        left, right = 0, len(numbers) - 1
        while left <= right:
            pivot = left + ((right - left) // 2)
            ## target found
            if numbers[pivot] == target:
                return pivot

            ## target belongs to ordered half
            elif ordered(left, pivot-1) and between(left, pivot-1):
                return binary_search(numbers, target, left, pivot-1)
            elif ordered(pivot+1, right) and between(pivot+1, right):
                return binary_search(numbers, target, pivot+1, right)

            ## target belongs in rotated half
            elif not ordered(left, pivot-1) and not between(pivot+1, right):
                left, right = left, pivot-1
            elif not ordered(pivot+1, right) and not between(left, pivot-1):
                left, right = pivot+1, right

            ## target cannot be found
            else:
                return -1

        return -1

