class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visit = set()

        def dfs(node):
            if node in visit:
                return 0, 0
            v, e = 0, 0
            visit.add(node)
            for n in graph[node]:
                ver, edg = dfs(n)
                v += ver
                e += edg
            return v+1, e+len(graph[node])

        res = 0
        for i in range(n):
            if i not in visit:
                v, e = dfs(i)
            
                if v*(v-1) == e:
                    res += 1
        return res