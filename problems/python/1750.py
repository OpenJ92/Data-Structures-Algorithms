class Solution:
    def minimumLength(self, string: str) -> int:
        def first(list):
            return list[0]
        def last(list):
            return list[-1]
        def valid(list):
            return len(list) > 1            \
               and first(list) == last(list)

        string = deque(list(string))
        while valid(string):
            landmark = string.popleft()
            while string and first(string) == landmark:
                string.popleft()
            while string and last(string) == landmark:
                string.pop()

        return len(string)
