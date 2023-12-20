class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            return sum(map(lambda x: ceil(x/k), piles)) <= h

        def binary_search():
            left = 1
            right = max(piles)

            while left <= right:
                mid = left + ((right - left) // 2)
                if check(mid):
                    right = mid - 1
                else:
                    left = mid + 1

            return left

        return binary_search()
