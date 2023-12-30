class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = defaultdict(int)
        for word in words:
            for char in word:
                counter[char] += 1

        n = len(words)
        for count in counter.values():
            if count % n != 0:
                return False
        return True
