class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        surround = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        q = deque()
        maze[entrance[0]][entrance[1]] = '+'
        entrance = tuple(entrance)
        # visited.add(entrance)
        q.append(entrance)
        d = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for x, y in surround:
                    r, c = row + x, col + y
                    if 0 <= r < len(maze) and 0 <= c < len(maze[r]) and maze[r][c] == '.':
                        if r == 0 or r == len(maze)-1 or c == 0 or c == len(maze[r])-1:
                            return d+1
                        q.append((r, c))
                        maze[r][c] = '+'
            d += 1
        return -1
