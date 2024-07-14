class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        cur, visited = 0, set()
        surround = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def dfs(row, col, prev):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or grid[row][col] != cur:
                return False
            if (row, col) in visited: return True
            visited.add((row, col))
            for x, y in surround:
                r, c = row+x, col+y
                if (r, c) != prev:
                    if dfs(r, c, (row, col)): return True

            return False
           
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited:
                    cur = grid[i][j]
                    if dfs(i, j, None): return True

        return False
        