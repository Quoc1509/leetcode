# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node, depth):
            if not node:
                return None, depth
            res1, left = dfs(node.left, depth+1)
            res2, right = dfs(node.right, depth+1)
            if left == right:
                return node, left
            if left < right:
                return res2, right
            if left > right:
                return res1, left
        res, d = dfs(root, 0)
        return res