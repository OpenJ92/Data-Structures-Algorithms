class Solution:
    def subarraysWithKDistinct(self, numbers: List[int], k: int) -> int:
        length = len(numbers)

        def window(frequency):
            counter, count, left = Counter(), 0, 0

            for right in range(length):
                counter[numbers[right]] += 1

                while left <= right and len(counter) > frequency:
                    counter[numbers[left]] -= 1
                    if not counter[numbers[left]]:
                        del counter[numbers[left]]
                    left += 1

                count += right - left + 1
            return count

        return window(k) - window(k-1)

