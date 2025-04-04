# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        maxD, res = 0, 0
        def dfs(node, d):
            nonlocal maxD, res
            if not node:
                maxD = max(d, maxD)
                return d
            l = dfs(node.left, d+1)
            r = dfs(node.right, d+1)

            if l == r == maxD:
                res = node
            return max(l, r)
        dfs(root, 0)
        return res