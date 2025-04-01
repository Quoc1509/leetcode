# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = defaultdict(list)

        def dfs(node, parent):
            if parent:
                adj[node.val].append(parent.val)
            if node.left:
                adj[node.val].append(node.left.val)
                dfs(node.left, node)
            if node.right:
                adj[node.val].append(node.right.val)
                dfs(node.right, node)
            
        dfs(root, None)     

        q = deque()
        q.append(target.val)
        visit = set()
        visit.add(target.val)
        while q and k > 0:
            print(q)
            for _ in range(len(q)):
                val = q.popleft()
                for no in adj[val]:
                    if no not in visit:
                        q.append(no)
                        visit.add(no)
            k -= 1
        return list(q)
            