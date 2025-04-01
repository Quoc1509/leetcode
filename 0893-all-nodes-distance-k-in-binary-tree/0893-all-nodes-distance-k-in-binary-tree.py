# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # adj = defaultdict(list)

        # def dfs(node, parent):
        #     if parent:
        #         adj[node.val].append(parent.val)
        #     if node.left:
        #         adj[node.val].append(node.left.val)
        #         dfs(node.left, node)
        #     if node.right:
        #         adj[node.val].append(node.right.val)
        #         dfs(node.right, node)
            
        # dfs(root, None)     

        # q = deque()
        # q.append(target.val)
        # visit = set()
        # visit.add(target.val)
        # while q and k > 0:
        #     for _ in range(len(q)):
        #         val = q.popleft()
        #         for no in adj[val]:
        #             if no not in visit:
        #                 q.append(no)
        #                 visit.add(no)
        #     k -= 1
        # return list(q)

        def restructure(node, parent):
            if not node:
                return

            node.parent = parent
            restructure(node.left, node)
            restructure(node.right, node)
        restructure(root, None)
        res = []
        visit = set()
        def dfs(node, k):
            if not node or node in visit:
                return
            if k == 0:
                res.append(node.val)
                return
            visit.add(node)
            dfs(node.left, k-1)
            dfs(node.right, k-1)
            dfs(node.parent, k-1)
        dfs(target, k)
        return res

            