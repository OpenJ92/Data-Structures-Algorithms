class Board:
    WinA = ['A', 'A', 'A']
    WinB = ['B', 'B', 'B']

    def __init__(self):
        self.rows = [[' ' for _ in range(3)] for _ in range(3)]
        self.columns = [[' ' for _ in range(3)] for _ in range(3)]
        self.diagonals = [[' ' for _ in range(3)] for _ in range(2)]

    def play(self, row, column, tile):
        self.rows[row][column] = tile
        self.columns[column][row] = tile
        if abs(row + column) == 2:
            self.diagonals[0][row] = tile
        if abs(row - column) == 0:
            self.diagonals[1][row] = tile

    def end(self):
        play_area = chain(self.rows, self.columns, self.diagonals)
        for area in play_area:
            if area == Board.WinB or area == Board.WinA:
                return True
        return False

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        game = Board(); count = len(moves)
        players = cycle(['A', 'B'])
        while moves:
            move, *moves = moves
            player = next(players)
            game.play(*move, player)
            if game.end():
                break
        if game.end():
            return player
        return "Draw" if count == 9 else "Pending"
