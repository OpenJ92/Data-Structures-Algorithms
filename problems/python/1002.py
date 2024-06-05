class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        def combine(counter, coumter):
            return counter & coumter

        counters = list(map(Counter, words))
        shared = reduce(combine, counters)

        output = ""
        for letter, count in shared.items():
            output += letter*count
        return "".join(output)

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counters = map(Counter, words)
        base, *counters = counters

        for counter in counters:
            base &= counter

        output = []
        for letter, frequency in base.items():
            output.extend([letter] * frequency)
        return output

