class Solution:
    def findTheDifference(self, string_one: str, string_two: str) -> str:
        counter_one = Counter(string_one)
        counter_two = Counter(string_two)

        for char in counter_two.keys():
            if counter_one[char] < counter_two[char]:
                return char

