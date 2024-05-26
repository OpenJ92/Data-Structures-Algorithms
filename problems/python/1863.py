class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def backtrack( nums: List[int], index: int, current_XOR: int) -> int:
            if index == len(nums): return current_XOR

            with_element = backtrack(nums, index + 1, current_XOR ^ nums[index])
            without_element = backtrack(nums, index + 1, current_XOR)

            return with_element + without_element

        return backtrack(nums, 0, 0)

class Solution:
    def subsetXORSum(self, numbers: List[int]) -> int:
        length, number, output = len(numbers), 0, 0

        def backtrack(index):
            nonlocal number
            nonlocal output

            if index == length:
                output += number
                return

            number ^= numbers[index]
            take = backtrack(index+1)
            number ^= numbers[index]

            skip = backtrack(index+1)

        backtrack(0)
        return output
