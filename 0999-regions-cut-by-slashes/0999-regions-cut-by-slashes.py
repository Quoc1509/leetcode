class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        father = {}
        rank = defaultdict(int)
        def root(x):
            if x not in father:
                father[x] = x
            if father[x] == x:
                return x
            return root(father[x])

        def union(a, b):
            a = root(a)
            b = root(b)

            if a == b:
                return
            if rank[a] > rank[b]:
                father[b] = a
            elif rank[a] < rank[b]:
                father[a] = b
            else:
                father[b] = a
                rank[a] += 1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                if grid[i][j] == ' ':
                    union((i,j, 0), (i, j, 1))
                    union((i, j, 1), (i, j, 2))
                    union((i, j, 2), (i, j, 3))
                elif grid[i][j] == '/':
                    union((i, j, 0), (i, j, 3))
                    union((i, j, 1), (i, j, 2))
                elif grid[i][j] == '\\':
                    union((i, j, 0), (i, j, 1))
                    union((i, j, 2), (i, j, 3))
                if i-1 >= 0:
                    union((i, j, 3), (i-1, j, 1))
                if j-1 >= 0:
                    union((i, j, 0), (i, j-1, 2))
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                for k in range(4):
                    if father[i, j, k] == (i, j, k):
                        count += 1
        return count


            