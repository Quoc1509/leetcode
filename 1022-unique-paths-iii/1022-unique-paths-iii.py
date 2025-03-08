class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start = None
        end = None
        obstacle = 0
        M, N = len(grid), len(grid[0])
        surround = [(1,0), (0, 1), (-1, 0), (0, -1)]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] == 2:
                    end = (i, j)
                if grid[i][j] == -1:
                    obstacle += 1
        visit = set()
        visit.add(start)
        res = [0]
        
        def BT(i, j):
            if (i, j) == end and len(visit) + obstacle == M*N:
                # print(visit)
                res[0] += 1
            
            for x, y in surround:
                r, c = i+x, j+y
                if 0 <= r < M and 0 <= c < N and (r, c) not in visit and grid[r][c] != -1:
                    visit.add((r, c))
                    BT(r, c)
                    visit.remove((r, c))
        BT(start[0], start[1])
        return res[0]