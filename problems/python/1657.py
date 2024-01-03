class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter_one = Counter(word1)
        counter_two = Counter(word2)

        count_one = list(counter_one.values())
        count_two = list(counter_two.values())
        count_one.sort()
        count_two.sort()

        letter_one = set(counter_one.keys())
        letter_two = set(counter_two.keys())

        return count_one == count_two and letter_one == letter_two
