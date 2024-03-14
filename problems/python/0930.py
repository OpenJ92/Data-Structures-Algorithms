class Solution:
    def numSubarraysWithSum(self, numbers: List[int], goal: int) -> int:
        def most(goal):
            left, current, total = 0, 0, 0
            for right in range(len(numbers)):
                current += numbers[right]

                while left <= right and current > goal:
                    current -= numbers[left]
                    left    += 1
                total += right - left + 1

            return total
    
        return most(goal) - most(goal - 1)
