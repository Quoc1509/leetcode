class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        counter = defaultdict(list)
        M, N = len(grid), len(grid[0])
        island = []
        surround = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def bfs(r, c):
            grid[r][c] = 0
            q = deque()
            q.append((r, c))
            island.append((r, c))
            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()
                    for a, b in surround:
                        ro, co = x+a, y+b
                        
                        if 0 <= ro < M and 0 <= co < N and grid[ro][co] == 1:
                            q.append((ro, co))
                            grid[ro][co] = 0
                            island.append((ro, co))  
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    island = []
                    bfs(i, j)
                    counter[len(island)].append(island)
        res = 0

        for key, item in counter.items():
            count = 0
            item = [sorted(i) for i in item]
            A = []
            for i in range(len(item)):
                land1 = item[i]
                ok = 1
                for j in range(len(A)):
                    land2 = A[j]
                    d1, d2 = -inf, -inf
                    k = 0
                    while k < len(land1):
                        a, b = land1[k]
                        c, d = land2[k]
                        if d1 == -inf:
                            d1 = a-c
                        elif a-c != d1:
                            break
                        if d2 == -inf:
                            d2 = b-d
                        elif b-d != d2:
                            break
                        k += 1
                    if k == len(land1):
                        ok = 0
                        break
                if ok:
                    A.append(land1)
            res += len(A)
                   

        return res
