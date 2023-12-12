class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        largestk = len(nums) - k + 1
        while largestk:
            kth = heappop(nums)
            largestk -= 1
        return kth
