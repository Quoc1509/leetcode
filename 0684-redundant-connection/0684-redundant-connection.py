class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        root = [i for i in range(len(edges))]
        rank = [0] * len(edges)
        def find(x):
            if root[x] == x:
                return x
            return find(root[x])
        
        def union(x, y):
            a = find(x-1)
            b = find(y-1)
            if a == b:
                return True
            if rank[a] < rank[b]:
                root[a] = b
                rank[b] += 1
            elif rank[b] < rank[a]:
                root[b] = a
                rank[a] += 1
            else:
                root[b] = a
                rank[a] += 1
                rank[b] += 1
            return False
        
        for a, b in edges:
            if union(a, b):
                return [a, b]
        return []








