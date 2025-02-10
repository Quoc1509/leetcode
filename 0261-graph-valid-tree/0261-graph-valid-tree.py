class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        def dfs(prev, node):
            
            visited.add(node)
            
            for n in graph[node]:
                if n != prev:
                    if n in visited: return False
                    if not dfs(node, n):
                        return False
            # visited.remove(node)
            
            return True
        
        return dfs(-1, 0) and len(visited) == n

        # rank = [0] * n
        # F = [i for i in range(n)]
        # def root(x):
        #     if F[x] == x:
        #         return x
        #     return root(F[x])
        
        # def union(a, b):
        #     rA = root(a)
        #     rB = root(b)

        #     if rA == rB:
        #         return False
        #     if rank[rA] < rank[rB]:
        #         F[rA] = rB
        #     elif rank[rB] < rank[rA]:
        #         F[rB] = rA
        #     else:
        #         F[rB] = rA
        #         rank[rA] += 1
        #     return True
        # for x, y in edges:
        #     if not union(x, y):
        #         return False
        # return len({root(i) for i in range(n)}) == 1

