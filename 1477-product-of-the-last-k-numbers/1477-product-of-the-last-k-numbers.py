class ProductOfNumbers:
    def __init__(self):
        self.product = [1]
        self.zero = -1
    def add(self, num: int) -> None:
        if num == 0:
            self.zero = len(self.product)
            self.product.append(self.product[-1])
            return
        self.product.append(self.product[-1]*num)

    def getProduct(self, k: int) -> int:
        if len(self.product)-k <= self.zero:
            return 0
        return self.product[-1]//self.product[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)