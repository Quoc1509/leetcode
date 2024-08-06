class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()

        def bfs(node):
            tmp = set()
            count = 1
            q = deque([node])
            visited.add(node)
            while q:
                for _ in range(len(q)):
                    n = q.popleft()
                    tmp.add(len(graph[n]))
                    for j in graph[n]:
                        if j not in visited:
                            visited.add(j)
                            count += 1
                            q.append(j)
            return len(tmp) == 1 and list(tmp)[0] == count -1
        res = 0
        for i in range(n):
            if i not in visited:
                # a, c = bfs(i)
                # b = list(a)
                # print(len(b), b)
                # if len(b) == 1 and b[0] == c-1:
                if bfs(i):
                    res += 1
        return res
        