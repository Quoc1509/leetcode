class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        count = 0
        father = [i for i in range(n)]
        rank = [1] * n
        size = [1] * n
        # temp = defaultdict(int)
        # for time, a, b in logs:
        #     temp[count] = time
        #     count += 1
        def root(x):
            if father[x] == x:
                return x
            return root(father[x])

        def union(a, b):
            rootA = root(a)
            rootB = root(b)
            if rootA == rootB:
                return
            if rank[rootA] < rank[rootB]:
                father[rootA] = rootB
                size[rootB] += size[rootA]
            elif rank[rootA] > rank[rootB]:
                father[rootB] = rootA
                size[rootA] += size[rootB]
            else:
                father[rootB] = rootA
                size[rootA] += size[rootB]
                rank[rootA] += 1
            if size[rootA] == n or size[rootB] == n:
                return True
            return False
        for time, a, b in logs:
            if union(a, b):
                return time
        return -1 
