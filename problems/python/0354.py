class TopDownTLE:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        length = len(envelopes)

        def valid(index, jndex):
            x, y = envelopes[index]
            u, v = envelopes[jndex]
            return (x < u and y < v)

        @cache
        def backtrack(index):
            longest = 1
            for jndex in range(index+1, length):
                if valid(index, jndex):
                    longest = max(longest, 1 + backtrack(jndex))
            return longest

        envelopes.sort()
        longest = -math.inf
        for index in range(length):
            longest = max(longest, backtrack(index))
        return longest

    
class BottomUpTLE:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        length = len(envelopes)
        dynamic = [1] * length
        
        def valid(index, jndex):
            x, y = envelopes[index]
            u, v = envelopes[jndex]
            return (x < u and y < v)

        envelopes.sort()
        for index in range(length-1,-1,-1):
            for jndex in range(index+1, length): 
                if valid(index, jndex):
                    dynamic[index] = max(1 + dynamic[jndex], dynamic[index])
        
        return max(dynamic)
