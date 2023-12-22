class Solution:
    def lengthOfLongestSubstringKDistinct(self, string: str, k: int) -> int:
        if not k:
            return 0

        left = 0
        max_length = -math.inf
        letters = defaultdict(int)

        for right in range(len(string)):
            letters[string[right]] += 1
            while left < right and len(letters) > k:
                letters[string[left]] -= 1
                if not letters[string[left]]:
                    del letters[string[left]]
                left += 1
            curr_length = (right - left + 1)
            max_length = max(curr_length, max_length)

        return max_length
