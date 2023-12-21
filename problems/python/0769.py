class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        intervals = []
        for index, value in enumerate(arr):
            interval = [index, value]
            interval.sort()
            heappush(intervals, tuple(interval))

        def merge(interval_left, interval_right):
            lower_left, upper_left = interval_left
            lower_right, upper_right = interval_right
            if upper_left < lower_right:
                return None
            return (min(lower_left,lower_right), max(upper_left,upper_right))

        stack = deque()
        while intervals:
            interval = heappop(intervals)

            if not stack:
                stack.append(interval)
                continue

            curr_interval  = stack.pop()
            merge_interval = merge(curr_interval, interval)
            if not merge_interval:
                stack.append(curr_interval)
                stack.append(interval)
            else:
                stack.append(merge_interval)

        return len(stack)
