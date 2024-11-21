class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        row = [(1, 0), (-1, 0)]
        col = [(0, 1), (0, -1)]
        
        visit = set((a, b) for a, b in guards)
        guards = set((a, b) for a, b in guards)
        walls = set([(a, b) for a, b in walls])
        
        def row(x, y):
            temp = x+1
            while temp < m:
                if (temp, y) in guards or (temp, y) in walls:
                    break
                visit.add((temp, y))
                temp += 1
            temp = x-1
            while temp >= 0:
                if (temp, y) in guards or (temp, y) in walls:
                    break
                visit.add((temp, y))
                temp -= 1

        def col(x, y):
            temp = y+1
            while temp < n:
                
                if (x, temp) in guards or (x, temp) in walls:
                    break
                visit.add((x, temp))
                temp += 1
                
            temp = y-1
            while temp >= 0:
                
                if (x, temp) in guards or (x, temp) in walls:
                    break
                visit.add((x, temp))
                temp -= 1
                
        

        for a, b in guards:
            row(a, b)
            col(a, b)
        # print(len(visit), len(walls))
        # print(visit)
        return m*n - len(visit) - len(walls)