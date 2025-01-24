class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = set()
        visit = set()
        def dfs(i):
            if i in safe or not graph[i]: 
                safe.add(i)
                return True
            if i in visit:
                return False
            visit.add(i)
            check = True
            for j in graph[i]:
                if not dfs(j):
                    check = False
            if check:
                safe.add(i)
            return check

        for i in range(len(graph)):
            if i not in visit:
                dfs(i)
                        
        return sorted(list(safe))
        