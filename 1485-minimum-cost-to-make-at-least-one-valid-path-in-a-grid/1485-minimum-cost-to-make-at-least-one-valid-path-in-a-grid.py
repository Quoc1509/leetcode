class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        surround = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = []
        visit = [[inf] * N for _ in range(M)]
        q.append((0, 0, 0))
        res = inf
        while q:
            cost, x, y = heappop(q)
            
            if x == M-1 and y == N-1:
                return cost
            if cost > visit[x][y]:
                continue
            for r, c in surround:
                ro, co = x+r, y+c
                change = 1
                if 0 <= ro < M and 0 <= co < N:
                    if grid[x][y] == 1 and c == 1:
                        change = 0
                    elif grid[x][y] == 2 and c == -1:
                        change = 0
                    elif grid[x][y] == 3 and r == 1:
                        change = 0
                    elif grid[x][y] == 4 and r == -1:
                        change = 0
                    if cost + change < visit[ro][co]:
                        visit[ro][co] = cost+change
                        heappush(q, (cost+change, ro, co))


            