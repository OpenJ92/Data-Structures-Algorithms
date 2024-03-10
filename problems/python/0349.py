class Solution:
    def intersection(self, num: List[int], bers: List[int]) -> List[int]:
        return set(num) & set(bers)
