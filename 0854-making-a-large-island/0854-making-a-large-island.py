class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        surround = [(1,0), (0,1), (-1,0), (0,-1)]
        visit = set()
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            land = []
            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()
                    land.append((x, y))
                    for ro, co in surround:
                        row, col = x+ro, y+co
                        if 0 <= row < M and 0 <= col < N and (row, col) not in visit and grid[row][col] != 0:
                            visit.add((row, col))
                            q.append((row, col))
            return land
        size = defaultdict(int)
        size[0] = 0
        lands = []
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1 and (i, j) not in visit:
                    temp = bfs(i, j)
                    lands.append(temp)
        res = 0
        for i in range(len(lands)):
            for a, b in lands[i]:
                grid[a][b] = (i+1)
                res = max(res, len(lands[i]))
            size[i+1] = len(lands[i])

        for i in range(M):
            for j in range(N):
                
                temp = 1
                s = set()
                if grid[i][j] == 0:
                    for r, c in surround:
                        row, col = i+r, j+c
                        if 0 <= row < M and 0 <= col < N and grid[row][col] not in s:
                            temp += size[grid[row][col]]
                            s.add(grid[row][col])
                    res = max(res, temp)
        # print(grid)
        return res