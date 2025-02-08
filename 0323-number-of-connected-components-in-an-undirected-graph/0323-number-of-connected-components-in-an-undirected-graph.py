class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [0] * n
        F = [i for i in range(n)]
        
        def root(x):
            if F[x] == x:
                return x
            return root(F[x])
        
        def union(a, b):
            a = root(a)
            b = root(b)
            if a == b: return
            if rank[a] < rank[b]:
                F[a] = b
                
            elif rank[b] < rank[a]:
                F[b] = a
                
            else:
                F[b] = a
                rank[a] += 1

        for a, b in edges:
            union(a, b)
        return len({root(i) for i in range(n)})