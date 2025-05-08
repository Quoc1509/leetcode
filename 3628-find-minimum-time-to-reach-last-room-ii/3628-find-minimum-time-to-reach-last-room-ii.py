class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        M, N = len(moveTime), len(moveTime[0])
        surround = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        d = [[inf]*N for _ in range(M)]
        heap = [(0, 1, 0, 0)]
        while heap:
            dis, second, x, y = heappop(heap)
            if d[x][y] < dis:
                continue
            for r, c in surround:
                i, j = x+r, y+c
                if 0 <= i < M and 0 <= j < N:                 
                    newD = max(dis, moveTime[i][j]) + second
                    newsecond = 3 - second
                    if newD < d[i][j]:
                        heappush(heap, (newD, newsecond, i, j))
                        d[i][j] = newD
        return d[-1][-1]