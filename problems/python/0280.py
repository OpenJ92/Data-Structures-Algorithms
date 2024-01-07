class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(array, index, jndex):
            temp = array[index]
            array[index] = array[jndex]
            array[jndex] = temp
            return

        nums.sort()
        for index in range(1, len(nums)-1, 2):
            swap(nums, index, index+1)

        return
