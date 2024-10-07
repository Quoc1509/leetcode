# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        delete = set(to_delete)
        res = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            dfs(node.right)
            if node.val in delete:
                if node.left and node.left.val not in delete:
                    res.append(node.left)
                if node.right and node.right.val not in delete:
                    res.append(node.right)
            if node.left and node.left.val in delete:
                node.left = None
            if node.right and node.right.val in delete:
                node.right = None
        dfs(root)
        if root.val not in delete:
            res.append(root)
        return res