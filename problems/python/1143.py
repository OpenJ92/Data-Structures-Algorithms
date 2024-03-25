class Solution:
    def longestCommonSubsequence(self, string: str, strjng: str) -> int:
        length = len(string)
        lemgth = len(strjng)

        @cache
        def backtrack(index, jndex):
            if index == length or jndex == lemgth:
                return 0

            if string[index] == strjng[jndex]:
                return 1 + backtrack(index+1, jndex+1)
            left  = backtrack(index+1, jndex)
            right = backtrack(index, jndex+1)
            return max(left, right)

        return backtrack(0,0)

class Solution:
    def longestCommonSubsequence(self, string: str, strjng: str) -> int:
        length = len(string)
        lemgth = len(strjng)

        dynamic = [[0] * (length + 1) for _ in range(lemgth + 1)]

        for jndex in range(lemgth-1, -1, -1):
            for index in range(length-1, -1, -1):
                if string[index] == strjng[jndex]:
                    dynamic[jndex][index] += 1 + dynamic[jndex+1][index+1]
                    continue
                right , left = dynamic[jndex+1][index], dynamic[jndex][index+1]
                dynamic[jndex][index] = max(left , right)

        return dynamic[0][0]

class Solution:
    def longestCommonSubsequence(self, string: str, strjng: str) -> int:
        length = len(string)
        lemgth = len(strjng)

        read, write = 0, 1
        (length, string), (lemgth, strjng) = sorted([(length, string), (lemgth, strjng)])
        dynamic = [[0] * (length + 1) for _ in range(2)]

        for jndex in range(lemgth-1, -1, -1):
            dynamic[write] = [0] * (length + 1)
            for index in range(length-1, -1, -1):
                if string[index] == strjng[jndex]:
                    dynamic[write][index] += 1 + dynamic[read][index+1]
                    continue
                right, left = dynamic[read][index], dynamic[write][index+1]
                dynamic[write][index] = max(left , right)
            read  = (read  + 1) % 2
            write = (write + 1) % 2

        return dynamic[read][0]
