class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
        visited = set()

        def dfs(city):
            if city in visited: return False
            temp = True
            visited.add(city)
            for j in graph[city]:
                if j not in visited:
                   temp = dfs(j)
            return temp
        res = 0
        for i in graph:
           if dfs(i): res += 1
        return res