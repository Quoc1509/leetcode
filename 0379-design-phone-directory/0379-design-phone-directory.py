class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.used = set()
        self.heap = [i for i in range(maxNumbers)]
        self.maxSize = maxNumbers

    def get(self) -> int:
        if len(self.used) < self.maxSize:
            num = heappop(self.heap)
            self.used.add(num)
            return num
        return -1

    def check(self, number: int) -> bool:
        if number in self.used:
            return False
        return True

    def release(self, number: int) -> None:
        if number in self.used:
            self.used.remove(number)
            heappush(self.heap, number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)