class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        M, N = len(heights), len(heights[0])
        surround = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        d = [[inf] * N for _ in range(M)]
        
        heap = [(0,0,0)]
        while heap:
            dif, r, c = heappop(heap)

            if r == M-1 and c == N - 1:
                return dif
            for x, y in surround:
                ro, co = r + x, c + y
                if 0 <= ro < M and 0 <= co < N:
                    new_dif = max(dif, abs(heights[r][c]-heights[ro][co]))
                    if d[ro][co] > new_dif:
                        d[ro][co] = new_dif
                        heappush(heap, (new_dif, ro, co))

        return 0
                