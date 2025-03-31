class Solution:

    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = []
        surround = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        M, N = len(grid), len(grid[0])
        heap.append([grid[0][0], 0, 0])
        visit = set()
        visit.add((0, 0))
        while heap:
            dist, r, c = heappop(heap)
            if r==M-1 and c==N-1:
                return dist
            for x, y in surround:
                ro, co = r+x, c+y
                if 0 <= ro < M and 0 <= co < N and (ro, co) not in visit:
                    temp = max(dist, grid[ro][co])
                    heappush(heap, [temp, ro, co])
                    visit.add((ro, co))
        return 0