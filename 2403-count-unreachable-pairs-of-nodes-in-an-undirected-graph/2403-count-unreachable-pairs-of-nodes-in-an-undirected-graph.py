class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def bfs(node):
            count = 1
            q = deque()
            q.append(node)
            visited.add(node)
            while q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    for ne in graph[cur]:
                        if ne not in visited:
                            q.append(ne)
                            visited.add(ne)
                            count += 1
            return count

        res, ans = 0, 0
        for i in range(n):
            if i not in visited: 
                group = bfs(i)  
                ans += group * res
                res += group
                
        return ans