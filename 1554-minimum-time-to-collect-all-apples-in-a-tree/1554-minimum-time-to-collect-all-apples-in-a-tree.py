class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        print(graph)
        def dfs(node, prev):
            res, path = hasApple[node], 0
            for i in graph[node]:
                if i != prev:
                    temp = dfs(i, node)
                    if temp[0]: 
                        res = True
                    path += temp[1]
            # print(res, path)
            if res == True:
                return (res, path+1)
            return (res, 0)
        a = dfs(0, -1)[1]
        return (a-1)*2 if a != 0 else 0