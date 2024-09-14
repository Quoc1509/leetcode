class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        M, N = len(matrix), len(matrix[0])
        dp = [[0]*N for _ in range(M)]
        res = 0
        for i in range(M):
            for j in range(N):
                length = int(matrix[i][j])
                if not (i == 0 or j == 0 or length == 0):
                    length = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
                dp[i][j] = length
                res = max(res, length*length)
        for r in dp:
            print(r)
        return res

