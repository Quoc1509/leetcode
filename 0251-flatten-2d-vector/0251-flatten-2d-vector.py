class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.M = len(self.vec)
        self.r = 0
        self.c = 0
    def idx(self): 
        if self.c + 1 >= len(self.vec[self.r]):
            self.c = 0
            self.r += 1  
        else:
            self.c += 1

    def next(self) -> int:
        while self.r < self.M and not self.vec[self.r]:
            self.idx()

        temp = self.vec[self.r][self.c]
        self.idx()
        return temp
        

    def hasNext(self) -> bool:
        while self.r < self.M and not self.vec[self.r]:
            self.idx()
            
        if self.r >= self.M or not self.vec[self.r]:
            return False
        return True


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()