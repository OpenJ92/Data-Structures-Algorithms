class Solution:
    def minDifficulty(self, job: List[int], days: int) -> int:
        length = len(job)
        if length < days:
            return -1

        @cache
        def backtrack(index, day):
            if day == days:
                return max(job[index:])

            hardest = 0 
            best = math.inf
            for difficulty in range(index, length - (days - day)):
                hardest = max(hardest, job[difficulty])
                best    = min(best, hardest + backtrack(difficulty + 1, day + 1))
            return best
        
        return backtrack(0, 1)

