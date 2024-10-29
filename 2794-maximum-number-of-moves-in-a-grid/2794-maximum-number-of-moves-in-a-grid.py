class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        moves = [(-1,1), (0, 1), (1, 1)]
        memo = {}
        res = [0]
        def dfs(r, c):
            if (r,c) in memo: return memo[(r, c)]
            count = -1
            for x, y in moves:
                ro, co = r+x, c+y
                if 0 <= ro < M and 0 <= co < N and grid[r][c] < grid[ro][co]:
                    count = max(count, dfs(ro, co))
            memo[(r, c)] = count+1
            res[0] = max(res[0], count + 1)
            return memo[(r, c)]

        for i in range(M):

            dfs(i, 0)
        return res[0]        
                

