class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        (_, freq), *items = counter.most_common()
        elements = takewhile(lambda uency: freq == uency[1], items)
        return freq + freq*len(list(elements))
