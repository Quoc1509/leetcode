class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        M, N = len(mat), len(mat[0])
        move = [(1, 0), (0, 1)]
        direct = 1
        q = deque()
        visit = set()
        q.append((0, 0))
        visit.add((0, 0))
        while q:
            temp = []
            for _ in range(len(q)):
                r, c = q.popleft()
                temp.append(mat[r][c])
                for x, y in move:
                    ro, co = r+x, c+y
                    if ro < M and co < N and (ro, co) not in visit:
                        q.append((ro, co))
                        visit.add((ro, co))
            if direct < 0:
                temp = temp[::-1]
            res.extend(temp)
            direct *= -1
        return res
