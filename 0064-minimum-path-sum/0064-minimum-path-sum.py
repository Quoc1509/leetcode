class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [[inf] * (N+1) for _ in range(M+1)]
        dp[1][0] = dp[0][1] = 0
        for i in range(1, M+1):
            for j in range(1, N+1):
                temp = min(dp[i-1][j], dp[i][j-1])
                dp[i][j] = temp + grid[i-1][j-1]
        return dp[-1][-1]