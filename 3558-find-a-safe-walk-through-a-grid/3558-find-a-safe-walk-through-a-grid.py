class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        M, N = len(grid), len(grid[0])
        visit = set()
        surround = [(1,0),(0,1),(-1,0),(0,-1)]
        @cache
        def dfs(row, col, k):
            if k == 0:
                return False
            if row == M-1 and col == N-1: return True
            check = False
            visit.add((row, col)) 
            for x, y in surround:
                r, c = row+x, col+y
                if 0 <= r < M and 0 <= c < N and (r, c) not in visit:
                    if grid[r][c] == 1:
                        k -= 1
                        if dfs(r, c, k):
                            check = True
                        k += 1
                    elif grid[r][c] == 0:
                        if dfs(r, c, k):
                            check = True
            visit.remove((row, col))
            return check
        if grid[0][0] == 1:
            health -= 1
        return dfs(0, 0, health)


                    