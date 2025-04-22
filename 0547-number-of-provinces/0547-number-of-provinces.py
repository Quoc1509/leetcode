class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        rank = [0]*N

        father = [i for i in range(N)] 
        def root(x):
            if x == father[x]:
                return x
            return root(father[x])

        def union(a, b):
            a = root(a)
            b = root(b)
            if a == b:
                return
            if rank[a] < rank[b]:
                father[a] = b
            elif rank[a] > rank[b]:
                father[b] = a
            else:
                father[b] = a
                rank[a] += 1
        
        for i in range(N):
            for j in range(N):
                if isConnected[i][j]: 
                    union(i, j)
        res = set()
        for i in range(N):
            res.add(root(i))
        print(father)
        return len(res)
    
        