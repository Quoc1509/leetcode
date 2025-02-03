# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        cur = [root]
        l = root.left
        r = root.right
        def dfs(node):
            if not node:
                return
            cur[0].right = TreeNode(node.val, None, None)
            cur[0].left = None
            cur[0] = cur[0].right
            dfs(node.left)
            dfs(node.right)
            # node.left = None
            # node.right = None
        dfs(l)
        dfs(r)
        