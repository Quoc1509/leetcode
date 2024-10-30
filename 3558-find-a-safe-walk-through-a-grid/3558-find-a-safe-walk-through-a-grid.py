class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n, m = len(grid), len(grid[0])
        if health == 1 and (grid[0][0] == 1 or grid[n - 1][m - 1] == 1):
            return False

        def isValid(x, y):
            return 0 <= x < n and 0 <= y < m and grid[x][y] != 2

        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = [(-(health - grid[0][0]), 0, 0)]
        grid[0][0] = 2

        while q:
            safe, r, c = heapq.heappop(q)
            safe = abs(safe)

            if r == n - 1 and c == m - 1 and safe > 0:
                return True


            for dx, dy in direction:
                x, y = r + dx, c + dy
                if isValid(x, y) and safe - grid[x][y] > 0:
                    heapq.heappush(q, (-(safe - grid[x][y]), x, y))
                    grid[x][y] = 2  # Mark as visited

        return False

                    