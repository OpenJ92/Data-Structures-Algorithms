class Solution:
    def convert(self, string: str, numRows: int) -> str:
        order = cycle([*range(numRows),*range(numRows-2, 0, -1)])

        letter_map = []
        for index, letter in enumerate(string):
            letter_map.append((next(order), index, letter))
        letter_map.sort()

        return "".join([letter for _, _, letter in letter_map])

