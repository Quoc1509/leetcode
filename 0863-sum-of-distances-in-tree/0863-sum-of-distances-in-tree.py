class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        dp = [0] * n
        child = [1] * n

        def dfs1(cur, par):
            for node in graph[cur]:
                if node != par:
                    dfs1(node, cur)
                    child[cur] += child[node]
                    dp[cur] += dp[node] + child[node]
        
        def dfs2(cur, par):
            for node in graph[cur]:
                if node != par:
                    dp[node] = dp[cur] + (n - 2*child[node])
                    dfs2(node, cur)
        dfs1(0, -1)
        dfs2(0, -1)
        
        return dp
            
            


        