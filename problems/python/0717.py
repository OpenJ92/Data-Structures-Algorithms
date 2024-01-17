class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        def dfs(index):
            if index == len(bits) - 1:
                return True
            if index == len(bits) - 2:
                return bits[index] == 0

            if bits[index] == 0:
                return dfs(index+1)
            else:
                return dfs(index+2)

        return dfs(0)
