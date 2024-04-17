class Solution:
    def searchRange(self, numbers: List[int], target: int) -> List[int]:

        def binary_search_left(array, value):
            left, right = 0, len(array)-1

            while left <= right:
                pivot = left + ((right - left) // 2)
                if array[pivot] >= value:
                    right = pivot - 1
                else:
                    left = pivot + 1

            return left

        def binary_search_right(array, value):
            left, right = 0, len(array)-1

            while left <= right:
                pivot = left + ((right - left) // 2)
                if array[pivot] <= value:
                    left = pivot + 1
                else:
                    right = pivot - 1

            return right

        binary_search = { 'left' : binary_search_left
                        , 'right' : binary_search_right
                        }

        if not numbers:
            return -1, -1

        length = len(numbers)
        left  = binary_search['left'](numbers, target)
        right = binary_search['right'](numbers, target)

        ################
        ## edge cases ##
        ################
        if not left and not right:
            if numbers[left] == target:
                return 0, 0
            return -1, -1

        if left == 0 and right == length - 1:
            if numbers[left] == target and numbers[right] == target:
                return left, right
            return -1, -1

        if left > right:
            return -1, -1

        if left == length or right == length:
            return -1, -1

        return left, right
