class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        q = deque()
        M, N = len(grid), len(grid[0])
        thierf = set()
        if grid[0][0] == 1 or grid[-1][-1] == 1: return 0
        surround = [(1,0), (0,1), (-1,0), (0,-1)]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    q.append((i, j))
                    thierf.add((i, j))
        count = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for a,b in surround:
                    ro, co = r+a, c+b
                    if 0 <= ro < M and 0 <= co < N and grid[ro][co] == 0:
                        q.append((ro, co))   
                        grid[ro][co] = count
            count += 1

        dist = [[0]*N for _ in range(M)]
        dist[0][0] = grid[0][0]
        heap = [(-dist[0][0], 0, 0)]
        while heap:
            d, i, j = heappop(heap)
            d = -d
            for a, b in surround:
                r, c = i+a, j+b
                if 0 <= r < M and 0 <= c < N and (r, c) not in thierf:
                    newDist = min(d, grid[r][c])
                    if dist[r][c] < newDist:
                        heappush(heap, (-newDist, r, c))
                        dist[r][c] = newDist

        return dist[-1][-1]
        