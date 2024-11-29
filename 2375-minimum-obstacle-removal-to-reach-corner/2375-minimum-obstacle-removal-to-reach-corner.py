class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        surround = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = []
        q.append((0, 0, 0))
        visit = set()
        visit.add((0, 0))
        while q:
            d, x, y = heappop(q)
            print(d, x, y)
            if x == M-1 and y == N-1:
                return d
            for a, b in surround:
                r, c = x+a, y+b
                if 0 <= r < M and 0 <= c < N and (r, c) not in visit:   
                    if grid[r][c] == 1:
                        heappush(q, (d+1, r, c))
                    else:
                        heappush(q, (d, r, c))
                    visit.add((r, c))

        return 0  
                    
