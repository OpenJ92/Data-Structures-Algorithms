class Recursive:
    def mostPoints(self, questions: List[List[int]]) -> int:
        length = len(questions)

        @cache
        def backtrack(index):
            if index >= length:
                return 0

            points, brainpower = questions[index]
            take = points + backtrack(index + brainpower + 1)
            skip = backtrack(index + 1)

            return max(take, skip)

        return backtrack(0)

class Iterative:

    def mostPoints(self, questions: List[List[int]]) -> int:
        length = len(questions)

        dynamic_program     = [0] * length
        dynamic_program[-1] = questions[-1][0]

        for index in range(length-2, -1, -1):
            take, brainpower = questions[index]
            next = index + brainpower + 1
            if  next < length:
                take += dynamic_program[next]
            skip = dynamic_program[index+1]

            dynamic_program[index] = max(take, skip)

        return dynamic_program[0]
