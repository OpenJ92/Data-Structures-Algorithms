class Solution:
    def customSortString(self, order: str, string: str) -> str:
        collect = defaultdict(list)
        others = []

        for letter in string:
            if letter in order:
                collect[letter].append(letter)
            else:
                others.append(letter)

        ordered_letters = []
        for letter in order:
            ordered_letters.append("".join(collect[letter]))

        return "".join([*ordered_letters, *others])
