class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.q = deque()
        if v1:
            self.q.append((0, 1))
        if v2:
            self.q.append((0, 2))

    def addNum(self, arr, i, check):
        if i < len(arr):
            self.q.append((i, check))

    def next(self) -> int:
        idx, check = self.q.popleft()
        if check == 1:
            num = self.v1[idx]
            self.addNum(self.v1, idx+1, check)
        else:
            num = self.v2[idx]
            self.addNum(self.v2, idx+1, check)
        return num

    def hasNext(self) -> bool:
        return self.q

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())