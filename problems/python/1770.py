class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        length = len(multipliers)
        nlength = len(nums)

        @cache
        def dynamic_program(left, index):
            if index >= length:
                return 0
            
            right = nlength - 1 - (index - left)

            _left  = nums[left]  * multipliers[index] \
		   + dynamic_program(left + 1, index + 1)

            _right = nums[right] * multipliers[index] \
		   + dynamic_program(left, index + 1)
        
            return max(_left, _right)
        

        @cache
        def dynamic_program(left, index, right):
            if index == length or right < 0:
                return 0

            _left = nums[left] * multipliers[index] \
                  + dynamic_program(left + 1, index + 1, right)
            _right = nums[right] * multipliers[index] \
                   + dynamic_program(left, index + 1, right - 1)
            
            return max(_left, _right)

        return dynamic_program(0, 0, nlength-1)

