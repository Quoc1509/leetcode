class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append((-succProb[i], edges[i][1]))
            graph[edges[i][1]].append((-succProb[i], edges[i][0]))

        dist = [0] * n
        dist[start_node] = -1
        q = []
        heapq.heappush(q, (-1, start_node))
        while q:
            w, n = heapq.heappop(q)
            if n == end_node:
                return -w
            if w > dist[n]: continue
            for we, ne in graph[n]:
                cur = -(we*w)
                if cur < dist[ne]:
                    heapq.heappush(q, (cur, ne))
                    dist[ne] = cur

        return 0