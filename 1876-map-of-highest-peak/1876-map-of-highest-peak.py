class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        surround = [(1,0),(0,1),(-1,0),(0,-1)]
        q = deque()
        M, N = len(isWater), len(isWater[0])
        visit = set()
        for i in range(M):
            for j in range(N):
                if isWater[i][j] == 1:
                    q.append((i, j))
                    visit.add((i, j))
        d = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                isWater[r][c] = d
                for ro, co in surround:
                    row, col = r+ro, c+co
                    if 0 <= row < M and 0 <= col < N and (row, col) not in visit:
                        q.append((row, col))
                        visit.add((row, col))
            d += 1

        return isWater
