class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        left, right, length = 0, 0, len(word)
        while right < length and word[right] != ch:
            right += 1

        if right == length:
            return word

        word = list(word)
        while left < right:
            word[left], word[right] = word[right], word[left]
            left, right = left + 1, right - 1

        return ''.join(word)

