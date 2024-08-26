class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        surround = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        res = 0
        M, N = len(grid), len(grid[0])
        
        def bfs(pos):
            q = deque()
            q.append(pos)
            check = True
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if r == 0 or r == M - 1 or c == 0 or c == N - 1:
                        check = False
                    for a, b in surround:
                        ro, co = r + a, c + b
                        if 0 <= ro < M and 0 <= co < N and grid[ro][co] == 0:
                            q.append((ro, co))
                            grid[ro][co] = 1
            return check

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    if bfs((i, j)): 
                        res += 1

        return res