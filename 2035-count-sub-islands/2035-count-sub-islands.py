class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        surround = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = 0
        M, N = len(grid1), len(grid1[0])
        def bfs(row, col):
            q = deque()
            q.append((row, col))
            check = True
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if grid1[r][c] == 0:
                        check = False
                    for x, y in surround:
                        ro, co = r+x, c+y
                        if 0 <= ro < M and 0 <= co < N and grid2[ro][co] == 1:
                            q.append((ro, co))
                            grid2[ro][co] = 0
            return check

        for i in range(M):
            for j in range(N):
                if grid1[i][j] == 1 and grid2[i][j] == 1:
                    if bfs(i, j):
                        # print(i, j)
                        res += 1

        return res