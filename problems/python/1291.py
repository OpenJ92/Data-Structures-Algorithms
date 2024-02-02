class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def order(number):
            count = 1
            while number // 10 > 0:
                number = number // 10
                count += 1
            return count

        def sequential(order):
            digits = '123456789'; numbers = []
            for digit in range(len(digits)-order+1):
                numbers.append(int(digits[digit:digit+order]))
            return numbers

        def produce_candidates(lower, upper):
            numbers = []
            for order in range(lower, upper+1):
                numbers = chain(numbers,sequential(order))
            return numbers


        candidates = deque(produce_candidates(order(low), order(high)))
        while candidates and candidates[0] < low:
            candidates.popleft()
        while candidates and candidates[-1] > high:
            candidates.pop()
        return candidates
