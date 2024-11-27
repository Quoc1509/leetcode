class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i in range(1, n):
            graph[i-1].append(i)
        res = []

        def bfs():
            count = 0
            q = deque([0])
            visit = set()
            visit.add(0)
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    if node == n - 1:
                        return count
                    for no in graph[node]:
                        if no not in visit:
                            q.append(no)
                            visit.add(no)
                count += 1
            return count

            

        for a, b in queries:

            graph[a].append(b)
            no = bfs()
            res.append(no)
    
        return res
