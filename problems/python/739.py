class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        days = [0] * len(temperatures)
        def last_recorded_temp(stack):
            return stack[-1][1]
        for day, temp in enumerate(temperatures):
            if not stack:
                stack.append((day, temp))
                continue

            while stack and temp > last_recorded_temp(stack):
                prev_day, prev_temp = stack.pop()
                days[prev_day] = day - prev_day

            stack.append((day, temp))

        return days
