class SegTree:
    def __init__(self, n, A=None):
        self.n = n
        self.L = [0] * (4*n)
        self.T = [0] * (4*n)
        if A:
            self.build(A)
        

    def push(self, t, tl, tr):
        T = self.T
        L = self.L
        if L[t] == 0:
            return 
        T[t] += L[t]
        if tl < tr:
            L[t*2] += L[t]
            L[t*2+1] += L[t]
        L[t] = 0

    def update(self, ql, qr, inc):
        self.update_(ql, qr, inc, 1, 0, self.n-1)

    def update_(self, ql, qr, inc, t, tl, tr):
        L,T = self.L, self.T
        self.push(t, tl, tr)
        if ql > tr or qr < tl:
            return 
        if ql <= tl and tr <= qr:
            L[t] += inc
            return 
        mi = (tl+tr)//2
        self.update_(ql, qr, inc, t*2, tl, mi)
        self.update_(ql, qr, inc, t*2+1, mi+1, tr)
        T[t] = T[t*2] + T[t*2+1]

    def query(self, ql, qr):
        return self.query_(ql, qr, 1, 0, self.n-1)
    
    def query_(self, ql, qr, t, tl, tr):
        L,T = self.L,self.T
        self.push(t, tl, tr)
        if ql > tr or qr < tl:
            return 0
        if ql <= tl and tr <= qr:
            return T[t]
        mi = (tl+tr) // 2
        l = self.query_(ql, qr, t*2, tl, mi)
        r = self.query_(ql, qr, t*2+1, mi+1, tr)
        return l + r
    
    def build(self, A):
        for i in range(len(A)):
            self.update(i,i,A[i])

class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v, w in edges:
            u -= 1
            v -= 1
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        t_in = [0] * n
        t_out = [0] * n
        value = [0] * n
        dist = [0]*n
        tim = -1
        def dfs(cur, par, weight):
            nonlocal tim
            tim += 1
            t_in[cur] = tim 
            dist[tim] = weight
            for ne, we in graph[cur]:
                if ne == par:
                    continue
                value[ne] = we
                dfs(ne, cur, we + weight)
            t_out[cur] = tim
        dfs(0, -1, 0)
        T = SegTree(n, dist)

        res = []
        for i in range(len(queries)):
            if queries[i][0] == 2:
                node = queries[i][1]-1
                res.append(T.query(t_in[node], t_in[node]))
            else:
                u, v, w = queries[i][1:]
                u -=1
                v -=1
                if t_in[u] > t_in[v]:
                    u,v = v, u
                inc = w - value[v]
                value[v] = w
                T.update(t_in[v], t_out[v], inc)
        
        return res