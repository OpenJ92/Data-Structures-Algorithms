class Solution:
    def lengthOfLIS(self, numbers: List[int]) -> int:
        length = len(numbers)

        @cache
        def backtrack(index):
            if index == length - 1:
                return 1
            take = 1
            for jndex in range(index + 1, length):
                if numbers[index] < numbers[jndex]:
                    take = max(take, 1 + backtrack(jndex))
            return take

        maximum = -math.inf
        for index in range(length):
            maximum = max(maximum, backtrack(index))
        return maximum

class Solution:
    def lengthOfLIS(self, numbers: List[int]) -> int:
        length = len(numbers)
        dynamic = [1] * (length)

        for index in range(length-1,-1,-1):
            for jndex in range(index+1, length):
                if numbers[index] < numbers[jndex]:
                    dynamic[index] = max(dynamic[index], 1 + dynamic[jndex])

        return max(dynamic)
