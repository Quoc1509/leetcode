class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        M, N = len(mat), len(mat[0])
        surround = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visit = set()
        for i in range(M):
            for j in range(N):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visit.add((i, j))
        dist = 1
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for x, y in surround:
                    ro, co = r+x, c+y
                    if 0 <= ro < M and 0 <= co < N and (ro, co) not in visit:
                        mat[ro][co] = dist
                        q.append((ro, co))
                        visit.add((ro, co))
            dist += 1
        return mat