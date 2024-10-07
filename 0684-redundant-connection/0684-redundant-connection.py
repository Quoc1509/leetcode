class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = [i for i in range(len(edges))]
        rank = [1] * len(edges)
        res = []
        def findRoot(x):
            if root[x] == x:
                return x
            return findRoot(root[x])

        for one, second in edges:
            a = findRoot(one-1)
            b = findRoot(second-1)

            if a == b:
                res = [one, second]
            if rank[a] < rank[b]:
                root[a] = b
            elif rank[a] > rank[b]:
                root[b] = a
            else:
                root[b] = a
                rank[a] += 1
        return res