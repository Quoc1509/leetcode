class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
                return False
            if (row, col) in visited or grid[row][col] == "0":
                return False
            visited.add((row, col))
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)
            return True
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if (r, c) not in visited and grid[r][c] == "1":
                    if dfs(r, c):
                        res += 1

        return res