class Solution:
    def removeVowels(self, string: str) -> str:
        strjng = []
        for letter in string:
            if letter not in 'aeiou':
                strjng.append(letter)
        return "".join(strjng)
