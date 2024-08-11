class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        n = start[0] if start[0] > target[0] else target[0]
        for i in range(len(specialRoads)):
            specialRoads[i]
            n = max(n, specialRoads[i][0], specialRoads[i][2])
        dis = defaultdict(int)
        graph = defaultdict(list)
        s = start[1]*n+start[0]
        e = target[1]*n+target[0]

        dis[s] = 0
        dis[e] = inf

        graph[s].append((abs(start[0]-target[0])+abs(start[1]-target[1]), e))
        for x1,y1,x2,y2,d in specialRoads:
            p1, p2 = y1*n+x1, y2*n+x2
            graph[p1].append((d, p2))
            if s != p1:
                graph[s].append((abs(start[0]-x1)+abs(start[1]-y1), p1))
            if e != p2:
                graph[p2].append((abs(target[0]-x2)+abs(target[1]-y2), e))
            dis[p1] = inf
            dis[p2] = inf
        for i in range(len(specialRoads)-1):
            x1, y1, x2, y2, d = specialRoads[i]
            p1, p2 = y1*n+x1, y2*n+x2
            for j in range(i+1, len(specialRoads)):
                a1, b1, a2, b2, w = specialRoads[j]
                k1, k2 = b1*n+a1, b2*n+a2
                we1 = abs(x2-a1) + abs(y2-b1)
                if we1 != 0:
                    graph[p2].append((we1, k1))
                    graph[k1].append((we1, p2))
                we2 = abs(x1-a2) + abs(y1-b2)
                if we2 != 0:
                    graph[p1].append((we2, k2))
                    graph[k2].append((we2, p1))

        # print(graph)
        heap = []
        heapq.heappush(heap, (0, s))
        while heap:
            we, no = heapq.heappop(heap)
            if we > dis[no]: continue
            for w, n in graph[no]:
                if w+we < dis[n]:
                    heapq.heappush(heap, (w+we, n))
                    dis[n] = w+we
        # print(dis)
        return dis[e]