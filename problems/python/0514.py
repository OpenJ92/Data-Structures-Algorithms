class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dictionary, circumference = [], len(ring)
        for index in range(len(ring)):
            dictionary.append((ring[index], index))
        dictionary.sort()

        def binary_search(array: List[int], value: int) -> List[int]:
            ''' Capture notches with desired value '''
            left, right = 0, len(array)

            while left <= right:
                pivot = left + ((right - left) // 2)
                if array[pivot][0] < value:
                    left = pivot + 1
                else:
                    right = pivot - 1

            indices = []
            while left < len(array) and array[left][0] == value:
                indices.append(array[left][1])
                left += 1

            return indices

        def forward(start: int, end: int):
            ''' Count notches to start to end going forward '''
            return abs(start - end)

        def backward(start: int, end: int):
            ''' Count notches to start to end going backward '''
            if start == end: return 0
            return circumference - forward(start, end)

        @cache
        def dyn(index, jndex):
            if jndex == len(key):
                return 0

            notches = binary_search(dictionary, key[jndex])

            minimum = inf
            for next in notches:
                step = min(forward(index, next), backward(index, next))
                turn = 1 + step + dyn(next, jndex+1)
                minimum = min(turn, minimum)

            return minimum

        return dyn(0,0)
