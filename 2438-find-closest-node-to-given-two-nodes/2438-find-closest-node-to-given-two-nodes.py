class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def dfs(node, n):
            visit = [-1] * n
            step = 0
            cur = node
            while cur != -1 and visit[cur] == -1:
                visit[cur] = step
                step += 1
                cur = edges[cur]
            return visit
        
        arr1 = dfs(node1, len(edges))
        arr2 = dfs(node2, len(edges))
        print(arr1, arr2)
        res = -1
        maxStep = inf
        for i in range(len(edges)):
            temp = max(arr1[i], arr2[i])
            if arr1[i]!= -1 and arr2[i]!= -1:
                if temp < maxStep:
                    maxStep = temp
                    res = i
        return res