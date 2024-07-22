class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        l = [inf] * n
        for x,y,z in times:
            graph[x].append((z, y))
        # print(graph)
        q = []
        heapq.heappush(q, (0, k))
        l[k-1] = 0
        while q:
            we, node = heapq.heappop(q)
            if we > l[node-1]: continue
            # print(we, node)
            for w, ne in graph[node]:
                if we + w < l[ne-1]:
                    heapq.heappush(q, (we+w, ne))
                    l[ne-1] = we+w
        res = 0
        for i in l:
            if i == inf: return -1
            res = max(res, i)
        return res
