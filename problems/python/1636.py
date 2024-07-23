class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        information, counter = [], Counter(nums)

        for number, frequency in counter.items():
            information.append((frequency, -number))
        information.sort()

        jndex = 0
        for index in range(len(information)):
            (frequency, number) = information[index]
            while frequency:
                nums[jndex] = -number
                frequency -= 1
                jndex += 1
        return nums

