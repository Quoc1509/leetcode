# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = ['']
        def dfs(node):
            if not node: return
            res[0] += '('
            res[0] += str(node.val)
            if not node.left and node.right:
                res[0] += '()'
            dfs(node.left)
            dfs(node.right)
            res[0] += ')'
        dfs(root)
        return res[0][1:len(res[0])-1]
        