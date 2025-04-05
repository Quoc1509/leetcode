class MaxStack:

    def __init__(self):
        self.count = 0
        self.stack = []
        self.minheap = []
        self.removed = set()

    def push(self, x: int) -> None:
        self.stack.append([x, self.count])
        heapq.heappush(self.minheap, (-x, -self.count))
        self.count += 1
        

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        num, count = self.stack.pop()
        self.removed.add(count)
        return num

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        while self.minheap and -self.minheap[0][1] in self.removed:
            heapq.heappop(self.minheap)
        return -self.minheap[0][0]

        

    def popMax(self) -> int:
        while self.minheap and -self.minheap[0][1] in self.removed:
            heapq.heappop(self.minheap)
        num, index = heapq.heappop(self.minheap)
        self.removed.add(-index)
        return -num
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()