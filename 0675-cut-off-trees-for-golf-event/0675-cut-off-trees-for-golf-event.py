class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        trees = sorted((v, r, c) for r, row in enumerate(forest)
                       for c, v in enumerate(row) if v > 1)
        print(trees)
        r = c = res = 0
        M, N = len(forest), len(forest[0])
        surround = [(1,0), (0,1), (-1,0), (0,-1)]
        def bfs(sr, sc, tr, tc):

            q = deque([(sr, sc, 0)])
            visit = {(sr, sc)}
            while q:
                for _ in range(len(q)):
                    ro, co, d = q.popleft()
                    if ro == tr and co == tc:
                        return d
                    for a, b in surround:
                        row, col = ro+a, co+b
                        if 0 <= row < M and 0 <= col < N and (row, col) not in visit and forest[row][col] != 0:
                            visit.add((row, col))
                            q.append((row, col, d+1))
            return -1

        for _, x, y in trees:
            dis = bfs(r, c, x, y)
            if dis < 0:
                return -1
            res += dis
            r, c = x, y
        return res
