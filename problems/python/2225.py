class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = {}
        losses = {}

        for win, loss in matches:
            self.update_count(wins, win)
            self.update_count(losses, loss)

        ans2 = []
        for player, loss in losses.items():
            if loss == 1:
                ans2.append(player)

        ans =  [ list(set(wins.keys()) - set(losses.keys()))
               , ans2
               ]

        ans[0].sort()
        ans[1].sort()
        return ans

    def update_count(self, hmap, value):
        if value not in hmap:
            hmap[value] = 1
        else:
            hmap[value] += 1
