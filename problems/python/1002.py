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
