class Solution:
    def countSubarrays(self, numbers: List[int], k: int) -> int:
        maximum, length, left = max(numbers), len(numbers), 0
        frequency, count = 0, 0

        for right in range(length):
            frequency += numbers[right] == maximum

            while frequency == k:
                frequency -= numbers[left] == maximum
                left += 1

            count += left

        return count

class Solution:
    def countSubarrays(self, numbers: List[int], k: int) -> int:
        maximum, length, left = max(numbers), len(numbers), 0
        frequency, count = 0, ((length + 1) * length) // 2

        for right in range(length):
            frequency += numbers[right] == maximum

            while left <= right and frequency >= k:
                frequency -= numbers[left] == maximum
                left += 1
            
            count -= right - left + 1
        
        return count
