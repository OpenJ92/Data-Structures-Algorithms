class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, columns, starts, length = len(board), len(board[0]), set(), len(word)
        board_characters, word_characters = Counter(), Counter(word)
        seen, directions = set(), [(1,0), (-1,0), (0,1), (0,-1)]

        for row in range(rows):
            for column in range(columns):
                if (character := board[row][column]) in word_characters:
                    board_characters[character] += 1
                    if character == word[0]:
                        starts.add((row, column))
        for character, frequency in word_characters.items():
            if board_characters[character] < frequency:
                return False
        
        def valid(row, column, index):
            return 0 <= row < rows and 0 <= column < columns            \
               and index < length and board[row][column] == word[index] \
               and (row, column) not in seen

        def backtrack(row, column, index):
            if not valid(row, column, index):
                return False

            if index == length - 1:
                return True

            seen.add((row,column))
            for drow, dcolumn in directions:
                nrow, ncolumn, nindex = row+drow, column+dcolumn, index+1
                if backtrack(nrow, ncolumn, nindex):
                    return True
            seen.remove((row,column))
            return False

        for row, column in starts:
            if backtrack(row, column, 0):
                return True
        return False
