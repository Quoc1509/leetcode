class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dfs(i, j):
            if i == m and j == n:
                return 1
            if i > m or j > n: return 0

            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(1, 1)
