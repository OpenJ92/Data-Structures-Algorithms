class Solution:
    def wordBreak(self, string: str, dictionary: List[str]) -> bool:
        dictionary = set(dictionary)
        length = len(string)

        @cache
        def backtrack(start, end):
            if end > length:
                return start + 1 == end

            _break = False
            if string[start:end] in dictionary:
                _break = True and backtrack(end, end)
            _continue = backtrack(start, end + 1)

            return _break or _continue

        return backtrack(0, 0)
