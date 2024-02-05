class Solution:
    def firstUniqChar(self, string: str) -> int:
        def first(elements):
            return elements[0]

        locations = defaultdict(list)
        for index, char in enumerate(string):
            locations[char].append(index)

        candidates = []
        for _, location in locations.items():
            if len(location) == 1:
                candidates.append(first(location))

        if candidates:
            heapify(candidates)
            return heappop(candidates)
        return -1
