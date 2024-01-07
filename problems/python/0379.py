class PhoneDirectory:
    ## This may be too space intensive.
    def __init__(self, max_numbers: int):
        self.numbers = [1 for _ in range(max_numbers)]

    def get(self) -> int:
        for index, available in enumerate(self.numbers):
            if available:
                self.numbers[index] = 0
                return index
        return -1

    def check(self, number: int) -> bool:
        return self.numbers[number] == 1

    def release(self, number: int) -> None:
        self.numbers[number] = 1


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
