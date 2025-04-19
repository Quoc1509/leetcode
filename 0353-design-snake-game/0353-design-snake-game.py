class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.visit = set()
        self.snake = deque()
        self.w = width
        self.h = height 
        # self.head = [0, 0]
        self.food = deque([(r, c) for r, c in food])
        self.visit.add((0, 0))
        self.snake.append((0, 0))
        print(self.food)
    def move(self, direction: str) -> int:
        headX, headY = self.snake[-1]
        if direction == 'U':
            headX -= 1
        elif direction == 'D':
            headX += 1
        elif direction == 'L':
            headY -= 1
        else:
            headY += 1
        next_move = (headX, headY)
        if headX < 0 or headX >= self.h or headY < 0 or headY >= self.w:
            return -1
         
        if self.food and next_move == self.food[0]:
            self.food.popleft()
        else:
            cord = self.snake.popleft()
            self.visit.remove(cord)
        self.snake.append(next_move)
        if next_move in self.visit:
            return -1
        self.visit.add(next_move)
        return len(self.snake)-1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)