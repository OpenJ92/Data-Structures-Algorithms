class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        letters = set([ 'a', 'b', 'c', 'd', 'e', 'f', 'g', \
                        'h', 'i', 'j', 'k', 'l', 'm', 'n', \
                        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', \
                        'w', 'x', 'y', 'z'])

        valid_words = set(wordList)

        if endWord not in valid_words:
            return 0

        def mutate(word, index):
            mutated_word = []
            nword = letters - set(word[index])
            for letter in nword:
                nword = word[:index] + letter + word[index+1:]
                if nword in valid_words:
                    mutated_word.append(nword)
            return mutated_word

        def construct_next_words(word):
            next_words = []
            for index in range(len(word)):
                next_words = chain(next_words, mutate(word, index))
            return next_words

        queue = deque([(beginWord, 1)])
        seen = set(beginWord)

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for mutated_word in construct_next_words(word):
                if mutated_word not in seen:
                    queue.append((mutated_word, steps+1))
                    seen.add(mutated_word)
        return 0
