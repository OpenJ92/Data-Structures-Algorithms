class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, string: str) -> int:
        left = 0
        max_length = -math.inf
        letters = defaultdict(int)

        for right in range(len(string)):
            letters[string[right]] += 1
            while left < right and len(letters) > 2:
                letters[string[left]] -= 1
                if not letters[string[left]]:
                    del letters[string[left]]
                left += 1
            curr_length = (right - left + 1)
            max_length = max(curr_length, max_length)

        return max_length
