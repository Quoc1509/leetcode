class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        N = 10**9+7
        dist = [inf] * n
        # visit = [0] * n
        
        graph = defaultdict(list)
        for a, b, c in roads:
            graph[a].append((c, b))
            graph[b].append((c, a))

        heap = [(0, 0)]
        dist[0] = 0
        # visit[0] = 1

        while heap:
            d, nod = heappop(heap)
            if d > dist[nod]:
                continue
            for dis, no in graph[nod]:
                # if d+dis == dist[no]:
                #     visit[no] = (visit[no] + visit[nod]) % N
                if d + dis < dist[no]:  
                    heappush(heap, (d+dis, no))
                    dist[no] = d+dis
                    # visit[no] = visit[nod]
        @cache
        def dfs(node):
            if node == n-1:
                return 1
            res = 0
            for w, no in graph[node]:
                if dist[node] + w == dist[no]:
                    res += dfs(no)
            return res%N
        return dfs(0) 

