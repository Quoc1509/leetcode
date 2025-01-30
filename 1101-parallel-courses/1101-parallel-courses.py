class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = [0] * n

        for a, b in relations:
            graph[a].append(b)
            indegree[b-1] += 1
        
        q = deque([i+1 for i in range(n) if indegree[i] == 0])

        res = 0
        while q:
            res += 1
            l = len(q)
            for _ in range(l):
                node = q.popleft()
                for n in graph[node]:

                    indegree[n-1] -= 1
                    if indegree[n-1] == 0:
                        q.append(n)

        return res if len(set(indegree)) == 1 and indegree[0]==0 else -1