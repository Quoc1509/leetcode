class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        move = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
        res = 0
        x = abs(x)
        y = abs(y)
        q = deque()
        q.append([x+y,0, 0])
        visit = set()
        visit.add((0,  0))
        minDis = x+y
        while q:
            for _ in range(len(q)):
                dis, r, c = q.popleft()
                if r == x and c == y:
                    return res
                for ro, co in move:
                    row, col = r+ro, c+co
                    new_dis = abs(x-row) + abs(y-col)
                    if new_dis > minDis + 3 or (row, col) in visit:
                        continue
                    minDis = min(new_dis, minDis)
                    q.append([new_dis,row, col])
                    visit.add((row, col))
            res += 1
        return -1