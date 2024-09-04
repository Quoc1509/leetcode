class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)] # M, E, S, W
        x, y = 0, 0
        res, direct = 0, 0
        obstacles = {(a, b) for a, b in obstacles}
        for i in commands:
            if i == -1:
                direct = (direct+1) % 4
            elif i == -2:
                direct = (direct-1) % 4
            else:
                dx, dy = direction[direct]
                for c in range(i):
                    if (x+dx, y+dy) in obstacles:
                        break
                    x += dx
                    y += dy
            res = max(res, x*x+y*y)
        return res


