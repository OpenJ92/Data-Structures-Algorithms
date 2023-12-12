class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapify(piles)

        while k:
            pile = -heappop(piles)
            reduce_pile = math.ceil(pile / 2)
            heappush(piles, -reduce_pile)
            k -= 1

        return -sum(piles)

