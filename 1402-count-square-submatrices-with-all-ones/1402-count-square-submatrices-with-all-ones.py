class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        dp = [[0]*(N+1) for _ in range(M+1)]
        res = 0
        for i in range(1, M+1):
            for j in range(1, N+1):
                if matrix[i-1][j-1] == 1:
                    length = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
                    dp[i][j] = length + 1
                    res += dp[i][j]
        return res