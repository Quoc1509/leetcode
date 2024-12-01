class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = deque()
        
        res = -inf
        for i in range(len(points)):
            while q and points[i][0] - points[q[0]][0] > k:
                q.popleft()
            if q:
                res = max(res, points[i][1]+points[q[0]][1]+abs(points[i][0]-points[q[0]][0]))
            while q and points[i][1] - points[i][0]>= points[q[-1]][1] - points[q[-1]][0]:                
                q.pop()
            q.append(i)
        return res
