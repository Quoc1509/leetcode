class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        surround = [(1,0), (0,1), (-1,0), (0,-1)]
        memo ={}
        M, N = len(matrix), len(matrix[0])
        def dfs(r, c):
            if (r, c) in memo: return memo[(r, c)]
            res = 0
            for x, y in surround:
                ro, co = r+x, c+y
                if 0 <= ro < M and 0 <= co < N and matrix[ro][co] > matrix[r][c]:
                    temp = dfs(ro, co)
                    res = max(res, temp)

            memo[(r, c)] = res + 1
            return memo[(r, c)]
        ans = 0
        for i in range(M):
            for j in range(N):
                count = dfs(i, j)
                ans = max(ans, count)

        return ans             


