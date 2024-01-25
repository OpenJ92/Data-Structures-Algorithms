class Solution:
    def maxLength(self, words: List[str]) -> int:
        augmented = []
        for word in words:
            if len(set(word)) == len(word):
                augmented.append(set(word))
        length = len(augmented)

        def backtrack(index, current):
            if index == length:
                return len(current)

            skip = backtrack(index+1, current); take = 0
            if augmented[index].isdisjoint(current):
                take = backtrack(index+1, current | augmented[index])

            return max(skip, take)

        return backtrack(0, set())
