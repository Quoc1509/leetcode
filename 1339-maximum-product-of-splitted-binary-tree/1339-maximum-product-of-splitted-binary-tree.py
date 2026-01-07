# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        def dfs1(node):
            if not node:
                return 0
            res = 0
            if node.left:
                res += dfs1(node.left)
            if node.right:
                res += dfs1(node.right)
            return res + node.val
        total = [dfs1(root)]
        ans = [0]

        def dfs2(node):
            if not node:
                return 0
            res = 0
            if node.left:
                res += dfs2(node.left)
            if node.right:
                res += dfs2(node.right)
            res += node.val
            ans[0] = max(ans[0], res*(total[0]-res))
            return res
        dfs2(root)
        return ans[0] % (10**9 + 7)