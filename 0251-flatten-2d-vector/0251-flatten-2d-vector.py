class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.r = 0
        self.c = -1
    def idx(self): 
        # if self.c + 1 >= len(self.vec[self.r]):
        #     self.c = 0
        #     self.r += 1  
        # else:
        #     self.c += 1
        r, c = self.r, self.c
        c += 1
        while r < len(self.vec) and(not self.vec[r] or c == len(self.vec[r])):
            r += 1
            c = 0
        return r, c

    def next(self) -> int:
        self.r, self.c = self.idx()
        return self.vec[self.r][self.c]    
    def hasNext(self) -> bool:
        r, c = self.idx()
        return r < len(self.vec) and c < len(self.vec[r])


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()