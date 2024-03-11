## class Solution:
##     def customSortString(self, order: str, string: str) -> str:
##         collect = defaultdict(list)
##         others = []
## 
##         for letter in string:
##             if letter in order:
##                 collect[letter].append(letter)
##             else:
##                 others.append(letter)
## 
##         ordered_letters = []
##         for letter in order:
##             ordered_letters.append("".join(collect[letter]))
## 
##         return "".join([*ordered_letters, *others])

class Solution:
    def customSortString(self, order: str, string: str) -> str:
        collect = Counter(string)

        ordered_letters = []
        for letter in order:
            ordered_letters.append(collect[letter] * letter)
            del collect[letter]
        for letter in collect:
            ordered_letters.append(collect[letter] * letter)

        return "".join(ordered_letters)

