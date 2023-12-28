class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        columns = len(board[0])

        count_column = defaultdict(lambda : defaultdict(int))
        count_row    = defaultdict(lambda : defaultdict(int))
        count_box    = defaultdict(lambda : defaultdict(int))

        for row, column in product(range(rows), range(columns)):
            element = board[row][column]
            if element == '.':
                continue

            count_column[column][element] += 1
            count_row[row][element]       += 1

            adjrow = (row    // 3)
            adjcol = (column // 3)
            count_box[(adjrow, adjcol)][element] += 1

            if count_column[column][element] == 2:
                return False
            if count_row[row][element] == 2:
                return False
            if count_box[(adjrow, adjcol)][element] == 2:
                return False

        return Tru
