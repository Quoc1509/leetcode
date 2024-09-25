class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        def dfs(prev, node):
            if node in visited: return False
            visited.add(node)
            
            for n in graph[node]:
                if n != prev:
                    
                    if not dfs(node, n):
                        return False
            # visited.remove(node)
            
            return True
        
        return dfs(-1, 0) and len(visited) == n

        
