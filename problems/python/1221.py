class Solution:
    def balancedStringSplit(self, string: str) -> int:
        counter = Counter()
        length = len(string)
        count = 0
        pointer = 0

        def balenced(counter):
            return counter['R'] == counter['L']

        while pointer < length:
            counter[string[pointer]] += 1

            if balenced(counter):
                pointer = pointer + 1
                count += 1
                counter = Counter()
                continue

            pointer += 1

        return count
