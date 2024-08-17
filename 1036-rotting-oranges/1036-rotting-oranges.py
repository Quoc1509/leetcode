class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rott = deque([])
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rott.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        if fresh == 0: return 0
        surround = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 1
        while rott:
            for _ in range(len(rott)):
                ro, co = rott.popleft()
                for x, y in surround:
                    row, col = ro + x, co + y
                    if 0 <= row < m and 0 <= col < n and grid[row][col] == 1:
                        grid[row][col] = 2
                        rott.append((row, col))
                        fresh -= 1
                        if fresh == 0:
                            return count
            count += 1
        return -1


        # for a, b in rott:
        #     bfs(a, b)
        # res = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == inf:
        #             return -1
        #         res = max(res, grid[i][j])
        # return res