class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        father = [i for i in range(n)]
        rank = [0] * n
        cost = [(1<<30)-1] * n

        def root(a):
            if a == father[a]:
                return a
            return root(father[a])

        def union(a, b, c):
            x = root(a)
            y = root(b)
            if x == y:
                cost[x] &= c
                return
            if rank[x] > rank[y]:
                rank[x] += 1
                father[y] = x
                cost[x] &= cost[y] & c
            elif rank[x] < rank[y]:
                rank[y] += 1
                father[x] = y
                cost[y] &= cost[x] & c
            else:
                father[y] = x
                rank[x] += 1
                cost[x] &= cost[y] & c
            
        for a, b, c in edges:
            union(a, b, c)

        res = []
        for a, b in query:
            if root(a) == root(b):
                res.append(cost[root(a)])
            else:
                res.append(-1)

        return res