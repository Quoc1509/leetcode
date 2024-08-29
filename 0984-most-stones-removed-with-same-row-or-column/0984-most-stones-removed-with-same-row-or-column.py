class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        xgraph = defaultdict(list)
        ygraph = defaultdict(list)
        for a, b in stones:
            xgraph[a].append((a, b))
            ygraph[b].append((a, b))
        
        count = [-1]
        visited = set()
        def dfs(x, y):
            count[0] += 1
            visited.add((x, y))
            for r, c in xgraph[x]:
                if (r, c) not in visited:
                    dfs(r, c)
            for r, c in ygraph[y]:
                if (r, c) not in visited:
                    dfs(r, c)
        res = 0
        for a, b in stones:
            count[0] = -1
            dfs(a, b)
            res += count[0]
        return res