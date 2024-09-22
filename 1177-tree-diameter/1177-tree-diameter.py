class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        print(graph)
        visited = set()
        res = [0] 
        def dfs(i):
            max1, max2 = 0, 0
            visited.add(i)
            for n in graph[i]:
                if n not in visited:
                    temp = dfs(n)
                    if temp > max1:
                        max2 = max1
                        max1 = temp
                    elif temp > max2:
                        max2 = temp
           
            res[0] = max(res[0], max1+max2)
            return max1 + 1

        dfs(0)
        return res[0]