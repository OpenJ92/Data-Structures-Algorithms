class Solution:
    def maxSlidingWindow(self, numbers: List[int], k: int) -> List[int]:
        maximums, right, length, output = deque(), 0,  len(numbers), []

        while right < length:
            if not maximums:
                maximums.append((right, numbers[right]))
                continue

            while maximums and numbers[right] >= maximums[-1][1]:
                maximums.pop()
            maximums.append((right, numbers[right]))

            if right >= k - 1:
                output.append(maximums[0][1])
                if maximums[0][0] == right - k + 1:
                    maximums.popleft()
            right += 1

        return output

