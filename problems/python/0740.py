class TopDown:
    def deleteAndEarn(self, numbers: List[int]) -> int:
        counter = Counter(numbers)
        numbers = range(min(numbers), max(numbers)+1)

        @cache
        def backtrack(index):
            if index >= len(numbers) or index < 0:
                return 0

            if counter[numbers[index]] == 0:
                return backtrack(index+1)

            number = numbers[index]
            take = counter[number] * number \
                 + backtrack(index+2)

            skip = backtrack(index+1)
            return max(take, skip)

        return backtrack(0)


class BottomUp:
    def deleteAndEarn(self, numbers: List[int]) -> int:
        counter = Counter(numbers)
        numbers = sorted(counter)

        if len(numbers) == 1:
            return counter[numbers[0]] * numbers[0]

        memo = [0] * len(numbers)
        memo[-1] = counter[numbers[-1]] * numbers[-1]

        if numbers[-1] - numbers[-2] == 1:
            memo[-2] = max( counter[numbers[-1]] * numbers[-1]               \
                          , counter[numbers[-2]] * numbers[-2]               \
                          )
        else:
            memo[-2] = counter[numbers[-1]] * numbers[-1]                    \
                     + counter[numbers[-2]] * numbers[-2]

        for index in range(len(numbers)-3,-1,-1):
            if numbers[index] + 1 == numbers[index+1]:
                memo[index] = max( counter[numbers[index]] * numbers[index] \
                                   + memo[index+2]                          \
                                 , memo[index+1]                            \
                                 )
            else:
                memo[index] = counter[numbers[index]]*numbers[index]        \
                            + memo[index+1]

        return memo[0]
