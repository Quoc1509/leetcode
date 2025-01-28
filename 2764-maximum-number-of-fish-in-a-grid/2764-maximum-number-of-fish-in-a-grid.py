class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        res = 0
        surround = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(ro, co):
            
            count = grid[ro][co]
            grid[ro][co] = 0
            for x, y in surround:
                row, col = ro+x, co+y
                if 0 <= row < M and 0 <= col < N and grid[row][col] != 0:
                    count += dfs(row, col)
            return count

        for i in range(M):
            for j in range(N):
                if grid[i][j] != 0:
                    res = max(res, dfs(i, j))
        # print(grid)
        return res