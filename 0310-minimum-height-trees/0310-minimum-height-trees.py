
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        # Build the graph
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
       
        q = deque()

        for key, item in graph.items():
            if len(item) == 1:
                q.append(key)

        while n > 2:
            for _ in range(len(q)):
                node = q.popleft()
                n-=1
                for ne in graph[node]:
                    graph[ne].remove(node)
                    if len(graph[ne]) == 1:
                        q.append(ne)

        return q
