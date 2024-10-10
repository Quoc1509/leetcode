class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        temp = set((x, y) for x, y in points)
        res = inf
        for i in range(len(points)-1):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                if (x1, y2) in temp and (x2, y1) in temp and x1 != x2 and y1 != y2:
                    res = min(res, abs((x1-x2)*(y1-y2)))
                    
        return res if res != inf else 0