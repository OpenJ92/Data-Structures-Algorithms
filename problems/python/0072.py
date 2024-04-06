class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length, lemgth = len(word1), len(word2)

        @cache
        def backtrack(one, two):
            if one == length:
                return lemgth - two
            if two == lemgth:
                return length - one

            if word1[one] == word2[two]:
                return backtrack(one+1, two+1)

            delete  = 1 + backtrack(one+1, two)
            insert  = 1 + backtrack(one, two+1)
            replace = 1 + backtrack(one+1, two+1)

            return min(delete, insert, replace)

        return backtrack(0,0)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length, lemgth = len(word1), len(word2)

        dynamic = [[0] * (lemgth + 1) for __ in range(length + 1)]
        for two in range(lemgth+1):
            dynamic[length][two] = lemgth - two
        for one in range(length+1):
            dynamic[one][lemgth] = length - one
        
        for two in range(lemgth-1,-1,-1):
            for one in range(length-1,-1,-1):
                if word1[one] == word2[two]:
                    dynamic[one][two] = dynamic[one+1][two+1]
                    continue
                delete = 1 + dynamic[one+1][two]
                insert = 1 + dynamic[one][two+1]
                replace = 1 + dynamic[one+1][two+1]

                dynamic[one][two] = min(delete, insert, replace)

        return dynamic[0][0]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length, lemgth = len(word1), len(word2)
        if not length and not lemgth:
            return 0
        
        (length, word1), (lemgth, word2) = sorted([(length, word1), (lemgth, word2)])
        dynamic = [[length - one for one in range(length+1)] for __ in range(2)]

        for two in range(lemgth-1,-1,-1):
            pointer, pojnter = two % 2, (two + 1) % 2
            dynamic[pointer][length] = lemgth - two
            for one in range(length-1,-1,-1):
                if word1[one] == word2[two]:
                    dynamic[pointer][one] = dynamic[pojnter][one+1]
                    continue
                delete  = dynamic[pointer][one+1]
                insert  = dynamic[pojnter][one]
                replace = dynamic[pojnter][one+1]
                dynamic[pointer][one] = 1 + min(delete, insert, replace)
        
        return dynamic[0][pointer]
        
