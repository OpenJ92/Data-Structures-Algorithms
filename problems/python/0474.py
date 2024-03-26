class Solution:
    def findMaxForm(self, strings: List[str], zeros: int, ones: int) -> int:
        counters = []
        for string in strings:
            counters.append(Counter(string))
        length = len(strings)

        @cache
        def backtrack(one, zero, index):
            if index >= length:
                return 0

            take = 0
            if counters[index]['1'] <= one and counters[index]['0'] <= zero:
                take = 1 + backtrack(one - counters[index]['1'], zero - counters[index]['0'], index + 1)
            skip = backtrack(one, zero, index + 1)

            return max(take, skip)

        return backtrack(ones, zeros, 0)

class Solution:
    def findMaxForm(self, strings: List[str], zeros: int, ones: int) -> int:
        counters = []
        for string in strings:
            counter = {}
            counter['0'] = string.count('0')
            counter['1'] = string.count('1')
            counters.append(counter)
        length = len(strings)

        @cache
        def backtrack(one, zero, index):
            if index >= length:
                return 0

            take = 0
            (_, zeros), (_, ones), *_ = counters[index].items()
            if ones <= one and zeros <= zero:
                take = 1 + backtrack(one - ones, zero - zeros, index + 1)
            skip = backtrack(one, zero, index + 1)

            return max(take, skip)

        return backtrack(ones, zeros, 0)

class Solution:
    def findMaxForm(self, strings: List[str], zeros: int, ones: int) -> int:
        counters = []
        for string in strings:
            counter = {}
            counter['0'] = string.count('0')
            counter['1'] = string.count('1')
            counters.append(counter)
        length = len(strings)

        @cache
        def backtrack(one, zero, index):
            if index >= length:
                return 0

            take = 0
            zeros, ones = counters[index]['0'], counters[index]['1']
            if ones <= one and zeros <= zero:
                take = 1 + backtrack(one - ones, zero - zeros, index + 1)
            skip = backtrack(one, zero, index + 1)

            return max(take, skip)

        return backtrack(ones, zeros, 0)
