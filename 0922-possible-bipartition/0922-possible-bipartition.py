class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        q = deque()
        group = [set(), set()]
        for key, item in graph.items():
            if key not in group[0] and key not in group[1]:
                q.append((key, 0))
                group[0].add(key)
                while q:
                    for _ in range(len(q)):
                        parents, num = q.popleft()
                        temp = 0 if num == 1 else 1
                        for c in graph[parents]:
                            if c in group[num]: return False
                            if c not in group[0] and c not in group[1]: q.append((c, temp))
                            group[temp].add(c)
                        
        return True