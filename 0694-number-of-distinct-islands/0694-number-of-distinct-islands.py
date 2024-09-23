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
            # item = [sorted(i) for i in item]
            # item.sort()
            print(item)
            A = []
            for land1 in item:
                ok = 1
                for land2 in A:
                    B = set([(a-c,b-d) for (a,b),(c,d) in zip(land1, land2)])
                    if len(B) == 1:
                        ok = 0
                        break
                if ok:
                    A.append(land1)
            res += len(A)
                   

        return res
