class Solution:
    def maximumLength(self, string: str) -> int:
        length = len(string)
        if length < 3:
            return -1

        valid_counter = Counter()
        right = 0
        left  = 0

        while right < length:
            if string[left] == string[right]:
                right += 1
                continue
            valid_counter[(string[left], len(string[left:right]))] += 1
            left = right
        valid_counter[(string[left], len(string[left:right]))] += 1

        secondary_counter = Counter()
        for (substring, l), count in valid_counter.items():
            for size in range(1, l):
                secondary_counter[(substring[0], size)] += count * (l - size + 1)
        valid_counter += secondary_counter

        max_length = -1
        for (substring, l), count in valid_counter.items():
            if count >= 3:
                max_length = max(l, max_length)

        return max_length
