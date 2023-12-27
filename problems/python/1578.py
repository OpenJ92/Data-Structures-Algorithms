class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        stack = deque()
        total_time = 0

        for color, time in zip(colors, neededTime):

            if not stack:
               stack.append((color, time))
               continue

            first_color, first_time = stack.pop()
            if color == first_color:
                most_time = max(time, first_time)
                stack.append((color, most_time))
                total_time += min(time, first_time)
            else:
                most_time = time
                stack.append((color, most_time))

        return total_time
