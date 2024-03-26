class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        length = len(pairs)

        def valid(pair, pajr):
            x, y = pair
            u, v = pajr
            return x > v or u > y

        @cache
        def backtrack(index):
            if index == length - 1:
                return 1
            take = 1
            for jndex in range(index + 1, length):
                if valid(pairs[index], pairs[jndex]):
                    take = max(take, 1 + backtrack(jndex))
            return take

        pairs.sort()
        maximum = -math.inf
        for index in range(length):
            maximum = max(maximum, backtrack(index))
        return maximum

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        def valid(pair, pajr):
            x, y = pair
            u, v = pajr
            return x > v or u > y

        pairs.sort()
        length = len(pairs)
        dynamic = [1] * length
        for index in range(length-1, -1, -1):
            for jndex in range(index+1, length):
                if valid(pairs[index], pairs[jndex]):
                    dynamic[index] = max(dynamic[index], 1 + dynamic[jndex])

        return max(dynamic)
