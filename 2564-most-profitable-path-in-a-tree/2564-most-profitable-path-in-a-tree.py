class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def helper(arr):
            N = len(arr)
            for i in range(N//2):
                amount[arr[i][0]] = 0
            if N %2 != 0:
                amount[arr[N//2][0]] //= 2
        path = [(bob, amount[bob])]
        def dfs1(node, par):
            if node == 0:
                helper(path)
                return True
            for n in graph[node]:
                if n != par:
                    path.append((n, amount[n]))
                    if dfs1(n, node):
                        return True
                    path.pop()
        dfs1(bob, -1)
        res = [-inf]

        def dfs2(node, d, par):
            if len(graph[node]) == 1 and node != 0:

                res[0] = max(res[0], d)
            
            for n in graph[node]:
                if n != par:
                    dfs2(n, d + amount[n], node)
        dfs2(0, amount[0], -1)

        return res[0]