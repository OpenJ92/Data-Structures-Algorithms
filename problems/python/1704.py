class Solution:
    def halvesAreAlike(self, string: str) -> bool:
        length = len(string)
        left  = Counter(string[:length//2].lower())
        right = Counter(string[length//2:].lower())

        left_vowel = 0
        right_vowel = 0
        for vowel in 'aeiou':
            left_vowel += left[vowel]
            right_vowel += right[vowel]
        return left_vowel == right_vowel
