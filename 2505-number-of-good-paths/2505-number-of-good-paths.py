class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        if len(vals) == 1:
            return 1

        N = len(vals)

        edges.sort(key=lambda x: max(vals[x[0]], vals[x[1]]))
        uf = UF(vals)
        return sum(uf.union(a,b) for a,b in edges) + N


class UF:
    def __init__(self, vals):
        self.n = len(vals)
        self.p = [i for i in range(self.n)]
        self.r = [0] * self.n
        self.mx = vals.copy()
        self.cnt = [1] * self.n
    
    def find(self, x):
        if x == self.p[x]:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return 0
        if self.r[a] < self.r[b]:
            a,b = b,a
        self.p[b] = a
        
        if self.r[a] == self.r[b]:
            self.r[a] += 1

        if self.mx[a] == self.mx[b]:
            res = self.cnt[a] * self.cnt[b]
            self.cnt[a] += self.cnt[b]
            return res
        else:
            if self.mx[a] < self.mx[b]:
                self.cnt[a] = self.cnt[b]
                self.mx[a] = self.mx[b]
            return 0

        

