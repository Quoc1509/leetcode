class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        res, num = 0, inf
        for a, b, c in edges:
            graph[a].append((c, b))
            graph[b].append((c, a))
        
        def bfs(city):
            q = []
            visited = set()
            visited.add(city)
            heapq.heappush(q, (0, city))
            while q:
                w, c = heapq.heappop(q)
                visited.add(c)
                if len(visited) == n: return n
                for we, ne in graph[c]:
                    if ne not in visited and w+we <= distanceThreshold:
                        heapq.heappush(q, (w+we, ne))  
            return len(visited)

        for i in range(n):
            r = bfs(i)
            if r <= num:
                res = i
                num = r
        return res