class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        graph = defaultdict(list)
        for i in range(N-1):
            a, b = points[i]
            for j in range(i+1, N):
                c, d = points[j]
                d = abs(a-c)+abs(b-d)
                graph[i].append((d, j))
                graph[j].append((d, i))
        res = 0
        visit = set()
        heap = [(0, 0)]
        while heap:
            if len(visit) == N: return res
            w, node = heappop(heap)
            if node not in visit:
                res += w        
                visit.add(node)
            for we, n in graph[node]:
                if n not in visit:
                    heappush(heap, (we, n))
        return res