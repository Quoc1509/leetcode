# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        res = []
        def dfs(node, subTree):
            # if not node: return 
            if not node.left and not node.right:
                if sum(subTree) == targetSum:
                    res.append(subTree)
                return
            if node.left:
                dfs(node.left, subTree + [node.left.val])
            if node.right:
                dfs(node.right, subTree+ [node.right.val])

        dfs(root, [root.val])
        return res