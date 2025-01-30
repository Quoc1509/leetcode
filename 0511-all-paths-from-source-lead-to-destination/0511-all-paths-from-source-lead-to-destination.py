class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
        visit = [0] * n # 0 is not visited, 1 is visiting, 2 is visited
        def dfs(node):
            if visit[node] != 0:
                return visit[node] == 2          
            if not graph[node]:
                return node == destination
            visit[node] = 1
            for n in graph[node]:
                if not dfs(n):
                    return False
            visit[node] = 2
            return True
        
        return dfs(source)
        