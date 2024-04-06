class Solution:
    def numDistinct(self, source: str, destination: str) -> int:
        length, lemgth = len(source), len(destination)

        @cache
        def backtrack(index, jndex):
            if jndex == lemgth:
                return 1
            if index == length:
                return 0

            count = backtrack(index+1,jndex)
            if source[index] == destination[jndex]:
                count += backtrack(index+1, jndex+1)
            return count

        return backtrack(0, 0)

class Solution:
    def numDistinct(self, source: str, destination: str) -> int:
        length, lemgth = len(source), len(destination)

        dynamic = [[0] * (lemgth + 1) for __ in range(length + 1)]
        for index in range(length + 1):
            dynamic[index][-1] = 1

        for index in range(length-1,-1,-1):
            for jndex in range(lemgth-1,-1,-1):
                dynamic[index][jndex] = dynamic[index+1][jndex]
                if source[index] == destination[jndex]:
                    dynamic[index][jndex] += dynamic[index+1][jndex+1]

        return dynamic[0][0]


class Solution:
    def numDistinct(self, source: str, destination: str) -> int:
        length, lemgth = len(source), len(destination)

        dynamic = [[0] * (lemgth + 1) for __ in range(2)]
        for index in range(2):
            dynamic[index][-1] = 1

        for index in range(length-1,-1,-1):
            read, write = (index + 1) % 2, index % 2
            for jndex in range(lemgth-1,-1,-1):
                dynamic[write][jndex] = dynamic[read][jndex]
                if source[index] == destination[jndex]:
                    dynamic[write][jndex] += dynamic[read][jndex+1]

        return dynamic[write][0]
