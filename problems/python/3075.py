class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        def relu(number):
            return max(number, 0)

        maximum, _ = 0, happiness.sort(reverse=True)
        for index in range(k):
            maximum += relu(happiness[index] - index)
        return maximum

