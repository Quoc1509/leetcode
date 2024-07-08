class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        size = len(grid)
        surround = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        land = deque()
        for i in range(size):
            for j in range(size):
                if grid[i][j] == 1:
                    land.append((i, j))
        if len(land) == 0 or len(land) == size * size: return -1

        res = 0
        while land:
            for _ in range(len(land)):
                row, col = land.popleft()
                for a, b in surround:
                    ro, co = row+a, col+b
                    if 0 <= ro < size and 0 <= co < size and grid[ro][co] != 1:
                        grid[ro][co] = 1
                        land.append((ro, co))
            res += 1

        return res-1