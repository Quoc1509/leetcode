class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        # graph = defaultdict(list)
        # for i in range(N-1):
        #     a, b = points[i]
        #     for j in range(i+1, N):
        #         c, d = points[j]
        #         d = abs(a-c)+abs(b-d)
        #         graph[i].append((d, j))
        #         graph[j].append((d, i))
        # res = 0
        # visit = set()
        # heap = [(0, 0)]
        # while heap:
        #     if len(visit) == N: return res
        #     w, node = heappop(heap)
        #     if node in visit:
        #         continue
        #     res += w        
        #     visit.add(node)
        #     for we, n in graph[node]:
        #         if n not in visit:
        #             heappush(heap, (we, n))
        # return res

        edges = []
        for i in range(N-1):
            a, b = points[i]
            for j in range(i+1, N):
                c, d = points[j]
                d = abs(a-c)+abs(b-d)
                edges.append([d, i, j])
        rank = [0] * N
        father = [i for i in range(N)]
        edges.sort()
        def root(x):
            if father[x] == x:
                return x
            return root(father[x])

        def union(a, b):
            if rank[a] < rank[b]:
                father[a] = b
            elif rank[a] > rank[b]:
                father[b] = a
            else:
                father[b] = a
                rank[a] += 1
        res = 0
        e = 0
        for w, a, b in edges:
            rootA = root(a)
            rootB = root(b)
            if rootA == rootB: continue
            e += 1
            union(rootA, rootB)
            res += w
            if e  == N-1:
                return res
        return res
        