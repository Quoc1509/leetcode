class Allocator:

    def __init__(self, n: int):
        self.memo = [-1] * n
        self.length = n
    def allocate(self, size: int, mID: int) -> int:
        i = 0
        while i < self.length:
            if self.memo[i] == -1:
                j = i
                while j < self.length and j < i+size and self.memo[j] == -1:
                    j += 1
                
                if j == i+size:
                    for k in range(i, j):
                        self.memo[k] = mID
                    return i
                i = j
            else:
                i += 1
        return -1

    def freeMemory(self, mID: int) -> int:
        count = 0
        for i in range(self.length):
            if self.memo[i] == mID:
                self.memo[i] = -1
                count += 1
        return count


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)