# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if len(nodes) == 1:
            return nodes[0]
        temp = set(nodes)
        
        res = None
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            l = dfs(node.left)

            r = dfs(node.right)
            a = l+r + (node in temp)
            if a == len(temp) and not res:
                res = node
            return a
        dfs(root)
        return res

