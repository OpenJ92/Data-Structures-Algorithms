class IterBFS:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = { '2' : 'abc'
                  , '3' : 'def'
                  , '4' : 'ghi'
                  , '5' : 'jkl'
                  , '6' : 'mno'
                  , '7' : 'pqrs'
                  , '8' : 'tuv'
                  , '9' : 'wxyz'
                  }

        if not digits:
            return []

        conversions = []
        stack = deque([(digits, "")])
        while stack:
            digits, conversion = stack.pop()
            if not digits:
                conversions.append(conversion)
                continue

            digit, *update_digits = digits
            for letter in letters[digit]:
                update_conversion = conversion + letter
                stack.append((update_digits, update_conversion))

        return conversions


class Product:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = { '2' : 'abc'
                  , '3' : 'def'
                  , '4' : 'ghi'
                  , '5' : 'jkl'
                  , '6' : 'mno'
                  , '7' : 'pqrs'
                  , '8' : 'tuv'
                  , '9' : 'wxyz'
                  }

        if not digits:
            return []

        conversions = []
        for num in digits:
            conversions.append(list(letters[num]))

        out = []
        for converted in product(*conversions):
            out.append("".join(converted))

        return out
