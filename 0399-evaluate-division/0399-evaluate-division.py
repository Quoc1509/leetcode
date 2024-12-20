class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        mp = defaultdict(list)
        for i in range(len(values)):
            mp[equations[i][0]].append((equations[i][1], values[i]))
            mp[equations[i][1]].append((equations[i][0], 1/values[i]))
        res = [-1.0]*len(queries)

        def bfs(x, y):
            q = deque()
            q.append((x, 1))
            visit = set()
            visit.add(x)
            while q:
                for _ in range(len(q)):
                    node, val = q.popleft()
                    if node == y:
                        return val
                    for n, v in mp[node]:
                        if n not in visit:
                            visit.add(n)
                            q.append((n, v*val))
            return -1.0
            
        for i in range(len(queries)):
            if queries[i][0] not in mp or queries[i][1] not in mp:
                continue
            val = bfs(queries[i][0], queries[i][1])
            res[i] = val
        print(res)
        return res