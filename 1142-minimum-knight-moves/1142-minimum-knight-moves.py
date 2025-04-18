class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        move = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
        res = 0
        q = deque()
        q.append([0, 0])
        visit = set()
        visit.add((0,  0))
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == x and c == y:
                    return res
                for ro, co in move:
                    row, col = r+ro, c+co
                    if (row, col) not in visit:
                        q.append([row, col])
                        visit.add((row, col))
            res += 1
        return -1