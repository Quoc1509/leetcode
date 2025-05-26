class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        visit = [0] * len(colors) 
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
        cycle = False
        dp = [[0] * 26 for _ in range(len(colors))]

        def dfs(cur):
            nonlocal cycle
            if visit[cur] == 1:
                cycle = True
                return [0] * 26
            if visit[cur] == 2:
                return dp[cur]
            visit[cur] = 1
            count = [0] * 26

            for ne in adj[cur]:
                if not cycle:
                    res = dfs(ne)
                    for i in range(26):
                        count[i] = max(count[i], res[i])

            count[ord(colors[cur])-ord('a')] += 1
            dp[cur] = count
            visit[cur] = 2
            return count
        res = 0
        for i in range(len(colors)):
            if visit[i] == 0:
                temp = dfs(i)
                res = max(res, max(temp))
        return -1 if cycle else res
