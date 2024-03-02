class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
      n = len(nums)
      squares = [0] * n

      left = 0
      right = n - 1
      index = n - 1

      while left <= right:
        if nums[left] ** 2 >= nums[right] ** 2:
          squares[index] += nums[left] ** 2
          left += 1
        else:
          squares[index] += nums[right] ** 2
          right -= 1
        index -= 1

      return squares

