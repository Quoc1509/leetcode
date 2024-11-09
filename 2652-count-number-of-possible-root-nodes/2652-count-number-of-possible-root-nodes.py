class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        guesses = set((a, b) for a, b in guesses)

        dp = [0] * len(graph)
        def dfs1(cur, par):
            count = 0
            for node in graph[cur]:
                if node != par:
                    if (cur, node) in guesses:
                        count += 1
                    count += dfs1(node, cur)
            dp[cur] = count
            return dp[cur]

        def dfs2(cur, par):
            for node in graph[cur]:
                if node != par:
                    dp[node] = dp[cur]
                    if (node, cur) in guesses:
                        dp[node] += 1
                    if (cur, node) in guesses:
                        dp[node] -= 1
                    dfs2(node, cur)

        dfs1(0, -1)   
        dfs2(0, -1)
        
        res = 0
        for i in dp:
            if i >= k:
                res += 1 
        return res