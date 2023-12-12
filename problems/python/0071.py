# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        path  = path.split('/')
        stack = []

        while path:
            segment, *path = path

            match segment:
                case "..":
                    if stack: stack.pop()
                case "." | "":
                    continue
                case _:
                    stack.append(segment)

        return "/" + "/".join(stack)
