class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # @cache
        # def dfs(i, j):
        #     if i == m and j == n:
        #         return 1
        #     if i > m or j > n: return 0

        #     return dfs(i+1, j) + dfs(i, j+1)
        # return dfs(1, 1)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        def get(dp, i, j):
            if i < 0 or j < 0:
                return 0
            return dp[i][j]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                dp[i][j] = get(dp, i-1, j) + get(dp, i, j-1)

        return dp[m-1][n-1]



