class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visit = set()
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            if node == destination:
                return True
            visit.add(node)
            for i in graph[node]:
                if i not in visit:
                    if dfs(i):
                        return True
            return False 
        
        return dfs(source)