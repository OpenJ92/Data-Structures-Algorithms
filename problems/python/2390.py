# https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, string: str) -> str:
        stack = []

        for char in string:
            if not stack:
                stack.append(char)
                continue

            if char == "*":
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
