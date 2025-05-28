class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        if k == 0:
            return [1] * (len(edges1)+1)
        def make_graph(edges):
            graph = defaultdict(list)
            for a, b in edges:
                graph[a].append(b)
                graph[b].append(a)
            return graph

        graph1 = make_graph(edges1)
        graph2 = make_graph(edges2)

        def bfs(graph, node, count):
            q = deque()
            q.append((node, -1))
            res = 1
            while q and count > 0:
                
                for _ in range(len(q)):
                    cur, pre = q.popleft()
                    for ne in graph[cur]:
                        if ne != pre:
                            q.append((ne, cur))
                count -= 1    
                res += len(q)
            return res

        def solution(graph, n, count):
            arr = [0] * (n+1)
            for i in range(n+1):
                arr[i] = bfs(graph, i, count)
            return arr

        arr1 = solution(graph1, len(edges1), k)
        arr2 = solution(graph2, len(edges2), k-1)

        maxF = max(arr2)
        for i in range(len(arr1)):
            arr1[i] += maxF

        return arr1