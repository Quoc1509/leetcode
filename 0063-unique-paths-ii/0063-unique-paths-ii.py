class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     i = len(obstacleGrid)
    #     j = len(obstacleGrid[0])
    #     visited = {}
    #     return self.countPath(obstacleGrid, i-1, j-1, visited)

    # def countPath(self, obstacleGrid, row, col, visited):
    #     key = str(row) + ", " + str(col)
    #     if key in visited: return visited[key]
    #     if row < 0 or col < 0 or obstacleGrid[row][col] == 1: return 0
    #     if row == 0 and col == 0: return 1
        
    #     visited[key] = self.countPath(obstacleGrid, row-1, col, visited) + self.countPath(obstacleGrid, row, col-1, visited)
    #     return visited[key]
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (N+1) for _ in range(M+1)]
        if obstacleGrid[0][0] == 1 or obstacleGrid[M-1][N-1] == 1:
            return 0
        dp[1][1] = 1
        for i in range(M):
            for j in range(N):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 0:
                    dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1]
        # print(dp[-1][-1])
        return dp[-1][-1]

