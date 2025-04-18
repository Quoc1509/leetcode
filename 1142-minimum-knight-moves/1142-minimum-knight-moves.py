MOVES = (
    (2, -1),
    (2, 1),
    (-2, 1),
    (-2, -1),
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2),
)

def getDirection(a):
    if a > 0:
        return 1
    elif a == 0:
        return 0
    else:
        return -1

class Solution:
    def minKnightMoves(self, tx: int, ty: int) -> int:
        if (tx, ty) == (0, 0):
            return 0

        visited = set()
        d = deque()
        d.append((0, 0, 0))

        while d:
            loc = d.popleft()
            x, y, move = loc
            px, py = getDirection(tx-x), getDirection(ty-y)

            for dx, dy in MOVES:
                nx, ny = x+dx, y+dy
                if (
                    (abs(tx - x) > 7 and px * dx < 0)  or (abs(ty - y) > 7 and py * dy < 0) or
                    (nx, ny) in visited
                ):
                    continue
                if nx == tx and ny == ty:
                    return move+1
                visited.add((nx, ny))
                d.append((nx, ny, move+1))
        return -1