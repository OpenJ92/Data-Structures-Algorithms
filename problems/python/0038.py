class Solution:
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
