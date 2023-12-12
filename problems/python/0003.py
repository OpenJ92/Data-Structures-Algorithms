# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0; right = 0;
        count = defaultdict(int)
        max_length = 0

        for right in range(len(s)):
            count[s[right]] += 1

            while count[s[right]] >= 2:
                count[s[left]] -= 1
                left += 1

            max_length = max(right - left + 1, max_length)

        return max_length
