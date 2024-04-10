class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:

        def valid(sweet):
            people, total = k + 1, 0
            for pieces in sweetness:
                total += pieces
                if total >= sweet:
                    people -= 1
                    total = 0
            return people <= 0

        left, right = min(sweetness), sum(sweetness) // (k + 1)
        while left < right:
            middle = 1 + left + ((right - left) // 2)
            if valid(middle):
                left = middle 
            else:
                right = middle - 1

        return right
