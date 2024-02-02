class TLE:
    def minWindow(self, string: str, ttring: str) -> str:
        def valid(counter):
            return all(map(lambda c: counter[c] >= tcounter[c], set(ttring)))

        @cache
        def dfs(left, right):
            if not valid(scounter):
                return None

            nonlocal least
            if len(least) > len(string[left:right]):
                least = string[left:right+1]

            scounter[string[right]] -= 1
            lefthand = dfs(left, right-1)
            scounter[string[right]] += 1

            scounter[string[left]] -= 1
            righthand = dfs(left+1, right)
            scounter[string[left]] += 1
        

        scounter = Counter(string)
        tcounter = Counter(ttring)
        left = 0; right = len(string) - 1
        least = string
        if not valid(scounter) or len(string) < len(ttring):
            return ""
            
        dfs(left, right)
        return least
