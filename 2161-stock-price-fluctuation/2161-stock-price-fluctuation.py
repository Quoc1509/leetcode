class StockPrice:

    def __init__(self):
        self.price = SortedList()
        self.mp = {}
        self.cur = -inf

    def update(self, timestamp: int, price: int) -> None: 
        if timestamp in self.mp:
            temp = self.mp[timestamp]
            self.price.remove(temp)
        self.mp[timestamp] = price
        self.price.add(price)
        if self.cur < timestamp:
            self.cur = timestamp


    def current(self) -> int:
        return self.mp[self.cur]

    def maximum(self) -> int:
        return self.price[-1]

    def minimum(self) -> int:
        return self.price[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()