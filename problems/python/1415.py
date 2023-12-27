class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        elements = ['a', 'b', 'c']
        possible = set(elements)
        happy = []

        def dfs(index, element, curr):
            if index == n:
                happy.append("".join(curr[:]))
                return

            for nelement in sorted(list(possible - set([element]))):
                curr.append(nelement)
                dfs(index+1, nelement, curr)
                curr.pop()

        dfs(0, '', [])
        if k > len(happy):
            return ""
        return happy[k-1]
