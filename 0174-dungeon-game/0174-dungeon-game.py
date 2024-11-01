class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        M, N = len(dungeon), len(dungeon[0])
        moves = [(1,0),(0,1)]
        @cache
        def dfs(r, c):
            if r == M-1 and c == N-1:
                return max(0, -dungeon[r][c])
            
            temp = inf
            for x, y in moves:
                ro, co = r+x, c+y
                if 0 <= ro < M and 0 <= co < N:
                    temp = min(temp, dfs(ro, co))
            temp -= dungeon[r][c]
            return max(0, temp)
        res = dfs(0, 0)
        return res+1