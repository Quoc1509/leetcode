class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
        visited = set()

        def dfs(city):
            visited.add(city)
            for j in graph[city]:
                if j not in visited:
                   temp = dfs(j)

        res = 0
        for i in graph:
           if i not in visited:
            dfs(i)
            res += 1
        return res