class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        restricted.add(0)
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        res = [0]
        def dfs(node):
            res[0] += 1
           
            for i in graph[node]:
                if i not in restricted:
                    restricted.add(i)
                    dfs(i)
        dfs(0)
        return res[0] 