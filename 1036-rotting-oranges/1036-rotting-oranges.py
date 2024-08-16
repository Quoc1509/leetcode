class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rott = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = inf
                if grid[i][j] == 2:
                    rott.append((i, j))
                    grid[i][j] = 0
        
        surround = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(r, c):
            visit = set()
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            count = 1
            while q:
                for _ in range(len(q)):
                    ro, co = q.popleft()
                    for x, y in surround:
                        row, col = ro + x, co + y
                        if 0 <= row < m and 0 <= col < n and grid[row][col] != 0 and (row, col) not in visit:
                            grid[row][col] = min(grid[row][col], count)
                            q.append((row, col))
                            visit.add((row, col))
                count += 1


        for a, b in rott:
            bfs(a, b)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == inf:
                    return -1
                res = max(res, grid[i][j])
        return res