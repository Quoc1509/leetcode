class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10**9+7
        @cache
        def dfs(i, j, lastRow):
            if i == n:
                return 1
            
            if j == m:
                return dfs(i+1, 0, lastRow) % mod

            row = list(lastRow)
            res = 0
            for color in range(0, 3):
                if color != lastRow[j] and color != (row[j-1] if j else -1):
                    row[j] = color
                    res = (res + dfs(i, j+1, tuple(row))) % mod
            return res
        row = [-1] * m
        return dfs(0, 0, tuple(row)) % mod