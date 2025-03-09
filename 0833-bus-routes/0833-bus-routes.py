class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].append(i)
        # print(graph)
        
        q = deque() 
        visit = set()
        for bus in graph[source]:
            q.append(bus)
            visit.add(bus)
        res = 1
        while q:
            for _ in range(len(q)):
                bus = q.popleft()
                for next_stop in routes[bus]:
                    if next_stop == target:
                        return res
                    for next_bus in graph[next_stop]:
                        if next_bus in visit:
                            continue
                        q.append(next_bus)
                        visit.add(next_bus)
            res += 1
        return -1