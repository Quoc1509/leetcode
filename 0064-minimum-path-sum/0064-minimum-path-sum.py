class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [[0] * (N+1) for _ in range(M+1)]
        for i in range(N+1):
            dp[0][i] = inf
        for i in range(M+1):
            dp[i][0] = inf
        dp[1][1] = grid[0][0]
        for i in range(1, M+1):
            for j in range(1, N+1):
                if i == 1 and j == 1:
                    continue
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
        # print(dp)
        return dp[-1][-1]