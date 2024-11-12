class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        ts = [0] * len(graph)
        def dfs1(cur, par):
            first = second = 0
            for node in graph[cur]:
                if node != par:
                    temp = dfs1(node, cur)
                    if temp > first:
                        second = first
                        first = temp
                    elif temp > second:
                        second = temp
            ts[cur] = [first, second]
            return first + (2 if cur % 2 == 0 else 1)

        dp = [0] * len(graph)

        def dfs2(cur, par, tf):
            w2 = 2 if cur % 2 == 0 else 1
            for node in graph[cur]:
                
                if node != par:
                    tf2 = 0
                    w = 1
                    if node % 2 == 0:
                        w = 2
                    if ts[node][0] + w == dp[cur]:
                        dp[node] = max(ts[node][0], w2+max(tf, ts[cur][1]))
                        tf2 = w2+max(tf, ts[cur][1])
                    else:
                        dp[node] = max(ts[node][0], w2+dp[cur])
                        tf2 = w2+dp[cur]
                    dfs2(node, cur, tf2)
        dfs1(0, -1)
        

        dp[0] = ts[0][0]
        dfs2(0, -1, 0)
        return dp