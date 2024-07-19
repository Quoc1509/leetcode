class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        
        def dfs(node, pre):
            res = 0
            apple = hasApple[node]
            for i in graph[node]:
                if i != pre:
                    temp = dfs(i, node)
                    if temp[1]: apple = True
                    res += temp[0]
            if apple:
                return (res+1, apple)
            return (res, apple)
        ans = dfs(0, -1)
        return (ans[0]-1)*2 if ans[1] else 0