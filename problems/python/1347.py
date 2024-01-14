class Solution:
    def minSteps(self, string: str, other: str) -> int:
        count_string = defaultdict(int)
        count_other  = defaultdict(int)
        chars = set()
        for char, dhar in zip(string, other):
            count_string[char] += 1
            count_other[dhar]  += 1
            chars.add(char)
            chars.add(dhar)

        out = 0
        for char in chars:
            if count_string[char] > count_other[char]:
                out += count_string[char] - count_other[char]

        return out
