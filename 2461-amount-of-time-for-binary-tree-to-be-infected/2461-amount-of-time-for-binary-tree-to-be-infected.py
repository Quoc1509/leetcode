# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        def dfs(cur, par):
            if cur.left:
                graph[cur.val].append(dfs(cur.left, cur.val))
            if cur.right:
                graph[cur.val].append(dfs(cur.right, cur.val))
            if par:
                graph[cur.val].append(par)
            return cur.val
        dfs(root, None)
        
        visit = set()
        q = deque()
        q.append(start)
        visit.add(start)
        count  = -1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for no in graph[node]:
                    if no not in visit:
                        q.append(no)
                        visit.add(no)
            count += 1
        return count
