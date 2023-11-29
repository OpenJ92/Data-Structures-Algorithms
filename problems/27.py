## https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        front = 0; back = len(nums) - 1; count = len(nums)

        while front <= back:
            if nums[front] != val:
                front += 1
            else:
                nums = self.swap(nums, front, back)
                back -= 1; count -= 1

        return count

    def swap(self, lst, front, back):
        lst[front], lst[back] = lst[back], lst[front]
        return lst
