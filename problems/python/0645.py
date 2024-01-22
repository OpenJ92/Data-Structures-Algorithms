class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        length = len(nums)
        lost, repeat = None, None
        for number in range(1, length+1):
            if counter[number] == 0:
                lost = number
            if counter[number] > 1:
                repeat = number
            if lost and repeat:
                break

        return [repeat, lost]
