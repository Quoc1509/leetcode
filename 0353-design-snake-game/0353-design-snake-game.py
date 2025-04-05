class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.visit = set()
        self.length = deque()
        self.w = width
        self.h = height 
        self.head = [0, 0]
        self.food = food
        self.visit.add(tuple([0, 0]))
        self.length.append([0, 0])
        self.idx = 0

    def move(self, direction: str) -> int:
        if direction == 'U':
            self.head[0] -= 1
        elif direction == 'D':
            self.head[0] += 1
        elif direction == 'L':
            self.head[1] -= 1
        else:
            self.head[1] += 1
        if self.head[0] < 0 or self.head[0] >= self.h or self.head[1] < 0 or self.head[1] >= self.w:
            return -1

        if self.idx < len(self.food) and self.head == self.food[self.idx]:
            self.length.append(self.head[:])
            self.visit.add(tuple(self.head))
            self.idx += 1
        else:
            cord = self.length.popleft()
            self.visit.remove(tuple(cord))
            self.length.append(self.head[:])
            if tuple(self.head) in self.visit:
                return -1
            self.visit.add(tuple(self.head))

        return len(self.length)-1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)