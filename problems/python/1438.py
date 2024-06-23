class Solution:
    def longestSubarray(self, numbers: List[int], limit: int) -> int:
        maximums = deque()
        minimums = deque()
        left = 0
        maxumum = 0

        for right in range(len(numbers)):
            # Maintain the maximums in decreasing order
            while maximums and maximums[-1] < numbers[right]:
                maximums.pop()
            maximums.append(numbers[right])

            # Maintain the minimums in increasing order
            while minimums and minimums[-1] > numbers[right]:
                minimums.pop()
            minimums.append(numbers[right])

            # Check if the current window exceeds the limit
            while maximums[0] - minimums[0] > limit:
                # Remove the elements that are out of the current window
                if maximums[0] == numbers[left]:
                    maximums.popleft()
                if minimums[0] == numbers[left]:
                    minimums.popleft()
                left += 1

            maxumum = max(maxumum, right - left + 1)

        return maxumum
