class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles = deque(piles)

        total = 0
        while piles:
            _, _, mine = piles.popleft(), piles.pop(), piles.pop()
            total += mine

        return total
