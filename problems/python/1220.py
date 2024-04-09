class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7

        @cache
        def backtrack(index, vowel):
            if index == n - 1:
                return 1

            match vowel:
                case 'a':
                    permutations = backtrack(index+1,'e')
                case 'e':
                    permutations = backtrack(index+1,'a') + backtrack(index+1,'i')
                case 'i':
                    permutations = backtrack(index+1, 'a') + backtrack(index+1, 'e') \
                                 + backtrack(index+1, 'o') + backtrack(index+1, 'u')
                case 'o':
                    permutations = backtrack(index+1,'i') + backtrack(index+1,'u') 
                case 'u':
                    permutations = backtrack(index+1,'a')

            return permutations % mod

        return ( backtrack(0, 'a') + backtrack(0, 'e') \
               + backtrack(0, 'i') + backtrack(0, 'o') \
               + backtrack(0, 'u') ) % mod

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u, mod = 0, 1, 2, 3, 4, 10 ** 9 + 7
        dyn = [[1] * 5 for __ in range(n)]

        for index in range(n-2,-1,-1):
            for vowel in [a,e,i,o,u]:
                match vowel:
                    case 0:
                        dyn[index][a] = dyn[index+1][e] % mod
                    case 1:
                        dyn[index][e] = (dyn[index+1][a] + dyn[index+1][i]) % mod
                    case 2:
                        dyn[index][i] = (dyn[index+1][a] + dyn[index+1][e] + dyn[index+1][o] + dyn[index+1][u]) % mod
                    case 3:
                        dyn[index][o] = (dyn[index+1][i] + dyn[index+1][u]) % mod
                    case 4:
                        dyn[index][u] = dyn[index+1][a] % mod

        return sum(dyn[0]) % mod

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u, mod = 0, 1, 2, 3, 4, 10 ** 9 + 7
        dyn = [[1] * 5 for __ in range(2)]

        read, write = (n - 2 + 1) % 2, (n - 2) % 2
        for index in range(n-2,-1,-1):
            read, write = (index + 1) % 2, index % 2
            for vowel in [a,e,i,o,u]:
                match vowel:
                    case 0:
                        dyn[write][a] = dyn[read][e] % mod
                    case 1:
                        dyn[write][e] = (dyn[read][a] + dyn[read][i]) % mod
                    case 2:
                        dyn[write][i] = (dyn[read][a] + dyn[read][e] + dyn[read][o] + dyn[read][u]) % mod
                    case 3:
                        dyn[write][o] = (dyn[read][i] + dyn[read][u]) % mod
                    case 4:
                        dyn[write][u] = dyn[read][a] % mod

        return sum(dyn[write]) % mod
