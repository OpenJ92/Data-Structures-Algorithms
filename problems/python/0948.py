class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        max_score = 0
        score = 0
        left, right = 0, len(tokens)-1
        while left <= right:
            if tokens[left] <= power:
                score += 1
                power -= tokens[left]
                left += 1
            elif score >= 1:
                score -= 1
                power += tokens[right]
                right -= 1
            else:
                break
            max_score = max(score, max_score)
        return max_score
