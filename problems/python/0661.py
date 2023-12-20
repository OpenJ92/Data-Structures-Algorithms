class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img); columns = len(img[0])
        def valid(row, column):
            return 0 <= row < rows and 0 <= column < columns

        directions = list(product([-1,0,1], [-1,0,1]))
        def smooth(row, column):
            average = 0; count = 0
            for drow, dcol in directions:
                nrow, ncol = row + drow, column + dcol
                if valid(nrow, ncol):
                    average += img[nrow][ncol]
                    count += 1
            return math.floor(average/count)

        new_img = [[0 for _ in range(columns)] for _ in range(rows)]
        for row, column in product(range(rows), range(columns)):
            new_img[row][column] = smooth(row, column)

        return new_img
