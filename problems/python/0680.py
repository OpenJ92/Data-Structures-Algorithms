class Solution:
    def validPalindrome(self, string: str) -> bool:

        @lru_cache(None)
        def recur(string, left, right, k):
            if k < 0:
                return False

            if left >= right:
                return True

            if left == right-1:
                if string[left] != string[right]:
                    return k > 0

                if string[left] == string[right]:
                    return True

            if string[left] == string[right]:
                return recur(string, left+1, right-1, k)

            if string[left] != string[right]:
                return recur(string, left+1, right, k-1) or recur(string, left, right-1, k-1)

        return recur(string,0,len(string)-1,1)
