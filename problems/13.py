class Solution:
    def romanToInt(self, s: str) -> int:
        replaced = list(map(self.replace, s))
        return self.compress(replaced)

    def replace(self, s:str):
        return \
                {
                       "I" : 1,
                       "V" : 5,
                       "X" : 10,
                       "L" : 50,
                       "C" : 100,
                       "D" : 500,
                       "M" : 1000
                }[s]

    def compress(self, s):
        retval = 0
        while s:
            element = s.pop(0)
            if not s or element >= s[0]:
                retval += element
            elif element < s[0]:
                s[0] -= element
        return retval
