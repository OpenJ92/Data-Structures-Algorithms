class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        def palindrome(word):
            left  = 0; right = len(word) - 1
            while left < right:
                if word[left] != word[right]:
                    return False
                right -= 1
                left  += 1
            return True

        max_length = -math.inf
        for word in words:
            length = len(word)
            max_length = max(length, max_length)

        new_words = []
        for word in words:
            word_length = len(word)
            new_word = "".join([word, " "*(max_length - word_length)])
            new_words.append(new_word)

        diagonals = defaultdict(list)
        for index in range(len(new_words)):
            for jndex in range(len(new_words[index])):
                diagonals[index + jndex].append(new_words[index][jndex])

        for diagonal in diagonals.values():
            if not palindrome(diagonal):
                return False
        return True
