class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M, N = len(heights), len(heights[0])
        PO = deque()
        AO = deque()
        surround = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(N):
            PO.append((0, i))
            AO.append((M-1, i))
        for i in range(M):
            PO.append((i, 0))
            AO.append((i, N-1))
        
        def bfs(q, M, N):
            visit = {(a, b) for a, b in q}

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for x, y in surround:
                        ro, co = r+x, c+y
                        if 0 <= ro < M and 0 <= co < N and heights[ro][co] >= heights[r][c] and (ro, co) not in visit:
                            q.append((ro, co))
                            visit.add((ro, co))
            return visit
        
        visit1 = bfs(PO, M, N)
        visit2 = bfs(AO, M, N)
        
        return list(visit1&visit2)

        
