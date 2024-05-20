class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def backtrack( nums: List[int], index: int, current_XOR: int) -> int:
            if index == len(nums): return current_XOR

            with_element = backtrack(nums, index + 1, current_XOR ^ nums[index])
            without_element = backtrack(nums, index + 1, current_XOR)

            return with_element + without_element

        return backtrack(nums, 0, 0)
