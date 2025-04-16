class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        valid = set((a, b) for a, b in connections)
        visit = set()

        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        q = deque([0])
        visit.add(0)
        res = 0
        while q:
            for _ in range(len(q)):
                no = q.popleft()
                for ne in graph[no]:
                    if ne not in visit:
                        if (no, ne) in valid:
                            res += 1
                        q.append(ne)
                        visit.add(ne)
        return res
