# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def dfs(cur, par):
            if cur.left:
                graph[cur.val].append(dfs(cur.left, cur.val))
            if cur.right:
                graph[cur.val].append(dfs(cur.right, cur.val))
            if par != -1:
                graph[cur.val].append(par)
            return cur.val
        dfs(root, -1)

        res = []
        q = deque()
        q.append(target.val)
        visit = set()
        visit.add(target.val)
        
        while k >= 0:
            for _ in range(len(q)):
                node = q.popleft()
                if k == 0:
                    res.append(node)
                for n in graph[node]:
                    if n not in visit:
                        visit.add(n)
                        q.append(n)
            k -= 1

        return res