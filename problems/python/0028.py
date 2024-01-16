class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        for pointer_haystack in range(len(haystack)):
            for pointer_needle in range(len(needle)):
                if pointer_haystack + pointer_needle >= len(haystack):
                    break
                if haystack[pointer_haystack + pointer_needle] != needle[pointer_needle]:
                    break
            else:
                return pointer_haystack
        return -1
