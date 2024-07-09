class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        size = len(grid)
        surround = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        visited = set()
        def bfs(row, col):
            q = deque()
            q.append((row, col))
            visited.add((row, col))
            while q:
                for _ in range(len(q)):
                    a, b = q.popleft()
                    for x, y in surround:
                        r, c = a + x, b + y
                        if 0 <= r < size and 0 <= c < size and (r, c) not in visited and grid[r][c] == 1:
                            q.append((r, c))
                            visited.add((r, c))

        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1:
                    bfs(i, j)
                    break
            if visited: break
        land = deque(list(visited))
        res = 0
        while land:
            for _ in range(len(land)):
                ro, co = land.popleft()
                for x, y in surround:
                    r, c = ro + x, co + y
                    if 0 <= r < size and 0 <= c < size and (r, c) not in visited:
                        if grid[r][c] == 1:
                            return res
                        land.append((r, c))
                        visited.add((r, c))
            res += 1
        return res