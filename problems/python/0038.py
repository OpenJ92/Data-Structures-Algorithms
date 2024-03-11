class Recursive:
    def countAndSay(self, n: int) -> str:

        def count(list):
            if not list:
                return [['', '']]
            pointer = 0
            while pointer < len(list) and list[pointer] == list[0]:
              pointer += 1
            return [[str(pointer), list[pointer-1]], *count(list[pointer:])]

        def say(list):
            output = []
            for frequency, character in list:
                output.append(frequency+character)
            return "".join(output)

        output = "1"
        for _ in range(1, n):
            output = say(count(output))
        return output

class Iterative:
    def countAndSay(self, n: int) -> str:

        def count(list):
            left    = 0
            right   = 0
            length  = len(list)

            output = []
            while right < length:
                count = 0
                while right < length and list[left] == list[right]:
                    count += 1
                    right += 1
                output.append([str(count), list[left]])
                left = right
            return output

        def say(list):
            output = []
            for frequency, character in list:
                output.append(frequency+character)
            return "".join(output)

        output = "1"
        functions = [lambda number: say(count(number)) for _ in range(1, n)]
        for function in functions:
            output = function(output)
        return output
