class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        measurement = []
        for num in nums:
            measurement.append(((num-x)**2, num))

        heapify(measurement)
        output = []
        for measure, num in nsmallest(k, measurement):
            output.append(num)
        output.sort()
        return output
