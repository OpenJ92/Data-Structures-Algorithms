class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)

        heap = []
        for word, count in count.items():
            heap.append((-count, word))
        heapify(heap)

        most_common = []
        while k:
            _, word = heappop(heap)
            most_common.append(word)
            k -= 1

        return most_common
