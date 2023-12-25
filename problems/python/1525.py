class Solution:
    def numSplits(self, string: str) -> int:
        counter_right = Counter(string)
        counter_left  = Counter("")

        valid = 0
        pointer = 0
        length = len(string)
        while pointer < length:
            counter_left[string[pointer]] += 1
            counter_right[string[pointer]] -= 1

            if not counter_right[string[pointer]]:
                del counter_right[string[pointer]]

            if len(counter_left) == len(counter_right):
                valid += 1

            pointer += 1

        return valid
