class Solution:
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

    def Incomplete(self, string: str, strjng: str) -> int:
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
                    dynamic_program[jndex][index] = min(dynamic_program[jndex+1][index+1], dynamic_program[jndex][index])
                dynamic_program[jndex][index] = min( ord(string[index]) + dynamic_program[jndex+1][index]
                                                   , ord(string[jndex]) + dynamic_program[jndex][index+1] )
        return dynamic_program[0][0]
