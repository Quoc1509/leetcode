class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][0] < grid[0][1] - 1 and grid[0][0] < grid[1][0] - 1: 
            return -1
        surround = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        M, N = len(grid), len(grid[0])
        heap = [(0, 0, 0)]
        visit = set()
        visit.add((0, 0))
        while heap:
            print(heap[0])
            time, x, y = heappop(heap)
            if x == M-1 and y == N-1:
                return time
            time += 1
            for a, b in surround:
                r, c = x+a, y+b
                if 0 <= r < M and 0 <= c < N and (r, c) not in visit:
                    if grid[r][c] > time:
                        if (grid[r][c] - time) % 2 == 0:
                            heappush(heap, (grid[r][c], r, c))
                        else:
                            heappush(heap, (grid[r][c]+1, r, c))
                    else:
                        heappush(heap, (time, r, c))
                    visit.add((r, c))
        return -1
            