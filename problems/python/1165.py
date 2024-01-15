class BinarySearch:
    def calculateTime(self, keyboard: str, word: str) -> int:

        def binary_search(iter, target, key = lambda x: x[0]):
            left = 0
            right = len(iter) - 1

            while right > left:
                middle = left + ((right - left) // 2)
                if key(iter[middle]) == target:
                    return middle
                elif key(iter[middle]) < target:
                    left = middle + 1
                else:
                    right = middle - 1
            return left

        labeled_keyboard = []
        for position, key in enumerate(keyboard):
            labeled_keyboard.append((key, position))
        labeled_keyboard.sort()

        positions = [0]
        for letter in word:
            index = binary_search(labeled_keyboard, letter)
            position = labeled_keyboard[index][1]
            positions.append(position)

        out = 0
        for posi, tion in zip(positions, positions[1:]):
            out += abs(posi - tion)

        return out

class HashMap:
    def calculateTime(self, keyboard: str, word: str) -> int:

        labeled_keyboard = defaultdict(int)
        for position, key in enumerate(keyboard):
            labeled_keyboard[key] = position

        positions = [0]
        for letter in word:
            position = labeled_keyboard[letter]
            positions.append(position)

        out = 0
        for posi, tion in zip(positions, positions[1:]):
            out += abs(posi - tion)

        return out
