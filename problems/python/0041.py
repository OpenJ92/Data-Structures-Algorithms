class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numbers = set([num for num in nums if num > 0])
        if not numbers:
            return 1

        maximum = max(numbers)
        minimum = min(numbers)
        length  = len(numbers)

        if length == (maximum - minimum + 1):
            if minimum != 1:
                return 1
            return maximum + 1

        if 1 not in numbers:
            return 1
        for potential in range(minimum, maximum+1):
            if potential not in numbers:
                return potential

class CycleSort:
    def firstMissingPositive(self, numbers: List[int]) -> int:
        length = len(numbers)

        def valid(index):
            return 0 < numbers[index] <= length \
               and numbers[index] != numbers[numbers[index]-1]

        def swap(index, jndex):
            temporary = numbers[jndex]
            numbers[jndex] = numbers[index]
            numbers[index] = temporary

        index = 0
        while index < length:
            while valid(index):
                swap(index, numbers[index] - 1)
            index += 1

        for index in range(length):
            if numbers[index] != index + 1:
                return index + 1

        return length + 1
