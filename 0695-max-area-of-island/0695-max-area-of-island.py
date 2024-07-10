class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # surround = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # def bfs(row, col):
        #     land = deque()
        #     land.append((row, col))
        #     grid[row][col] = 0
        #     count = 1 
        #     while land:
        #         for _ in range(len(land)):
        #             ro, co = land.popleft()
        #             for a, b in surround:
        #                 r, c = ro + a, co + b
        #                 if 0 <= r < len(grid) and 0 <= c < len(grid[r]) and grid[r][c] == 1:
        #                     land.append((r, c))
        #                     grid[r][c] = 0
        #                     count += 1
        #     return count
        # res = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         if grid[i][j] == 1:
        #             temp = bfs(i, j)
        #             res = max(res, temp)

        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            return 1 + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col -1)
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    temp = dfs(i, j)
                    res = max(res, temp)


        return res