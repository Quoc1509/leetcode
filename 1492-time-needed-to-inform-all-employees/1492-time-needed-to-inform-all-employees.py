class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        res = [0]
        def dfs(node):
            if node not in graph:
                return 0
            res = 0
            for j in graph[node]:
                res = max(res, dfs(j))
            return res + informTime[node] 

        for i in range(len(manager)):
            if i == headID: continue
            graph[manager[i]].append(i)
        # print(graph)

        return dfs(headID)