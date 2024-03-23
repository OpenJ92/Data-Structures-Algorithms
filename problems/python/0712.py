class TopDown:
    def minimumDeleteSum(self, string: str, strjng: str) -> int:
        length = len(string)
        lemgth = len(strjng)

        @cache
        def backtrack(one, two):
            if one == length:
                return sum(map(ord, strjng[two:]))
            if two == lemgth:
                return sum(map(ord, string[one:]))

            minimum = math.inf
            if string[one] == strjng[two]:
                minimum = min(backtrack(one + 1, two + 1), minimum)

            minimum = min(ord(string[one]) + backtrack(one + 1, two), minimum)
            minimum = min(ord(strjng[two]) + backtrack(one, two + 1), minimum)

            return minimum

        return backtrack(0, 0)

class BottomUp:
    def minimumDeleteSum(self, string: str, strjng: str) -> int:
        length = len(string)
        lemgth = len(strjng)

        dynamic_program = [[math.inf] * (length+1) for _ in range(lemgth+1)]
        dynamic_program[lemgth][length] = 0

        for index in range(length-1, -1, -1):
            dynamic_program[lemgth][index] = dynamic_program[lemgth][index+1] + ord(string[index])
        for jndex in range(lemgth-1, -1, -1):
            dynamic_program[jndex][length] = dynamic_program[jndex+1][length] + ord(strjng[jndex])

        for index in range(length-1, -1, -1):
            for jndex in range(lemgth-1, -1, -1):
                if string[index] == strjng[jndex]:
                    minimum = min(dynamic_program[jndex+1][index+1], dynamic_program[jndex][index])
                    dynamic_program[jndex][index] = minimum
                minimum = min( ord(string[index]) + dynamic_program[jndex][index+1]
                             , ord(strjng[jndex]) + dynamic_program[jndex+1][index]
                             , dynamic_program[jndex][index] )
                dynamic_program[jndex][index] = minimum

        return dynamic_program[0][0]

class BottomUpSpaceOptimized:
    def minimumDeleteSum(self, string: str, strjng: str) -> int:
        length = len(string)
        lemgth = len(strjng)

        read, write = 0, 1
        (length, string), (lemgth, strjng) = sorted([(length, string), (lemgth, strjng)])
        dynamic_program = [[math.inf] * (length + 1) for _ in range(2)]
        dynamic_program[read][length] = 0

        for index in range(length-1, -1, -1):
            dynamic_program[read][index] = dynamic_program[read][index+1] \
                                         + ord(string[index])

        for jndex in range(lemgth-1, -1, -1):
            dynamic_program[write] = [math.inf] * (length + 1)
            dynamic_program[write][length] = dynamic_program[read][length] \
                                           + ord(strjng[jndex])
            for index in range(length-1, -1, -1):
                if string[index] == strjng[jndex]:
                    dynamic_program[write][index] = dynamic_program[read][index+1]
                minimum = min( ord(string[index]) + dynamic_program[write][index+1]
                             , ord(strjng[jndex]) + dynamic_program[read][index]
                             , dynamic_program[write][index] )
                dynamic_program[write][index] = minimum
            read  = (read  + 1) % 2
            write = (write + 1) % 2

        return dynamic_program[read][0]

