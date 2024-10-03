class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        surround = [(1,0), (0,1), (-1,0), (0,-1)]
        father = list(range(m*n))     
        rank = [0] * (m*n)

        def findRoot(x):
            if father[x] == x: return x
            return findRoot(father[x])

        def union(a, b):
            a = findRoot(a)
            b = findRoot(b)
            if a == b: return          
            if rank[a] < rank[b]:
                father[a] = b
            elif rank[a] > rank[b]:
                father[b] = a
            else:
                father[b] = a
                rank[a] += 1

        visited = set()
        cnt = 0
        res = []
        for i in range(len(positions)):
            x,y = positions[i]
            ind1 = x*n + y
            if ind1 in visited:
                res.append(cnt)
                continue
            tmp = set()
            for a,b in surround:
                ro, co = x+a, y+b
                ind2 = ro*n+co
                if 0 <= ro < m and 0 <= co < n and ind2 in visited:
                    tmp.add(findRoot(ind2))
            no_surround_island = len(tmp)
            cnt = cnt - (no_surround_island - 1)
            res.append(cnt)
            for a,b in surround:
                ro, co = x+a, y+b
                ind2 = ro*n+co
                if 0 <= ro < m and 0 <= co < n:
                    if ind2 in visited:
                        union(ind1, ind2)
            visited.add(ind1)

    
        return res
