class Logger:

    def __init__(self):
        self.hashMap = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.hashMap:
            self.hashMap[message] = timestamp
            return True
        if timestamp - self.hashMap[message] < 10:
            return False
        self.hashMap[message] = timestamp
        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)