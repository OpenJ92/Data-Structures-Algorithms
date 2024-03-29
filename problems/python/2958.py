class Solution:
    def maxSubarrayLength(self, numbers: List[int], k: int) -> int:
        left, length, counter = 0, len(numbers), Counter()

        output = 0
        for right in range(length):
            counter[numbers[right]] += 1

            while left < right and counter[numbers[right]] > k:
                counter[numbers[left]] -= 1
                left += 1

            output = max(output, right - left + 1)

        return output

